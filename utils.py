import pandas as pd
import os
import calendar

# Define global variable:
isced_education_mapping = {
    'Less than primary education': 'Less than a high school diploma',
    'Below upper secondary education': 'Less than a high school diploma',
    'Upper secondary education': 'High school graduates, no college',
    'Completion of intermediate upper secondary programmes': 'High school graduates, no college',
    'Post-secondary non-tertiary education': 'Some college or associate degree',
    'Short-cycle tertiary education': 'Some college or associate degree',
    'Bachelor’s or equivalent education': "Bachelor's degree",
    'Master’s or equivalent education': "Master's degree",
    'Doctoral or equivalent education': "Doctoral degree",
    'Primary education': 'Less than a high school diploma',
    'Tertiary education': "Bachelor's degree",
    'Upper secondary or post-secondary non-tertiary education': 'Some college or associate degree',
    'Lower secondary education': 'Less than a high school diploma',
    'Completion of intermediate lower secondary programmes': 'Less than a high school diploma'
}

european_countries = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium',
    'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic',
    'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece',
    'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Latvia',
    'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco',
    'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal',
    'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain',
    'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'Vatican City'
]

education_level_order = [
    'Less than a high school diploma',
    'High school graduates, no college',
    'Some college or associate degree',
    "Bachelor's degree",
    "Master's degree",
    "Doctoral degree"
]


def read_usbls_data(dir_path: str, file_name: str, blank_row: int) -> pd.DataFrame:
    """
       Reads an Excel file containing US Bureau of Labor Statistics data from the specified directory,
       skips the rows up to the specified blank row, and restructures the data into a long format with
       months and corresponding values under each age group (inferred from the file name) as columns.

       Parameters:
       dir_path (str): The directory path where the Excel file is located.
       file_name (str): The name of the Excel file, including the extension. The part before the extension
                        is used to label the data column for the age group.
       blank_row (int): The number of initial rows to skip in the Excel file (0-indexed), typically used to
                        skip header information or blank rows.

       Returns:
       pandas.DataFrame: A DataFrame indexed by 'Year' and 'Month' columns, with one additional column
                         representing the data for the specific age group, labeled by the file name prefix.

       """
    # Construct the full file path
    full_path = os.path.join(dir_path, file_name)
    # Read the Excel file
    df = pd.read_excel(full_path, skiprows=blank_row)

    month_column = df.columns.tolist()
    month_column.remove('Year')
    age_header = file_name.split('.')[0]

    # Restructure the data frame, unpivot the data, set year and month as index
    df = pd.melt(df, id_vars='Year', value_vars=month_column, var_name='Month', value_name=age_header)
    df.set_index(['Year', 'Month'], inplace=True)
    return df


def concatenate_usbls_files(dir_path: str, blank_row: int, year_range: tuple = (1980, 2024)):
    start_year, end_year = year_range
    combined_df = None
    files = os.listdir(dir_path)
    month_to_num = {name[:3]: num for num, name in enumerate(calendar.month_abbr) if num}
    for file in files:
        df = read_usbls_data(dir_path, file, blank_row)
        df.reset_index(inplace=True)
        df['Month'] = df['Month'].map(month_to_num)
        df.set_index(['Year', 'Month'], inplace=True)
        if combined_df is None:
            combined_df = df
        else:
            combined_df = pd.merge(combined_df, df, left_index=True, right_index=True, how='right')
    combined_df.sort_index(inplace=True)
    # Filter the data based on the year range
    combined_df = combined_df.loc[start_year:end_year]
    return combined_df


def read_eurostat_data(dir_path: str, file_name: str) -> pd.DataFrame:
    full_path = os.path.join(dir_path, file_name)
    df_eu_age = pd.read_excel(full_path, skiprows=10)
    df_eu_age = df_eu_age.iloc[1:-5]  # Remove last 5 rows
    df_eu_age = df_eu_age.filter(regex='^(?!Unnamed)')  # Remove Unnamed columns
    df_eu_age = df_eu_age.drop('TIME', axis=1)
    df_eu_age = df_eu_age.melt(var_name='Year', value_name=file_name.split('.')[0])
    df_eu_age.set_index('Year', inplace=True)
    return df_eu_age


def merge_eurostat_data(dir_path: str) -> pd.DataFrame:
    combined_df = None
    for file_name in os.listdir(dir_path):
        if file_name.endswith('.xlsx'):
            new_df = read_eurostat_data(dir_path, file_name)
        if combined_df is None:
            combined_df = new_df
        else:
            combined_df = pd.merge(combined_df, new_df, left_index=True, right_index=True, how='left')
    return combined_df


def process_onsgovuk_data(df_uk: pd.DataFrame) -> pd.DataFrame:
    """
    Processes data from the ONS (Office for National Statistics, UK) to calculate the average unemployment rates
    by ethnicity over time. This function cleans the data, converts time strings to datetime objects, ensures numeric
    representation of unemployment values, groups data by time and ethnicity, and then restructures it into a pivot table format.

    Parameters:
    df_uk (pd.DataFrame): A DataFrame containing UK unemployment data from OnsGovUK.

    Returns:
    pd.DataFrame: A pivot table DataFrame indexed by 'time' (datetime), with columns for each ethnicity category, containing
                  average unemployment rates.

    DocTest:
    >>> data = {'time': ['Jan2020', 'Jan2020', 'Feb2020', 'Feb2020'],
    ...         'ethnicity': ['Asian', 'Black', 'Asian', 'Black'],
    ...         'value': ['5', '6', '4', '7']}
    >>> df_uk = pd.DataFrame(data)
    >>> processed_df = process_onsgovuk_data(df_uk)
    >>> print(repr(processed_df))
    ethnicity   Asian  Black
    time
    2020-01-01    5.0    6.0
    2020-02-01    4.0    7.0
    """
    df_uk['time'] = pd.to_datetime(df_uk['time'].str.split('-').str[0], format='%b%Y')  # Extract the month and year
    # Ensure the 'value' column is numeric
    df_uk['value'] = pd.to_numeric(df_uk['value'], errors='coerce')
    # Group the data by 'time' and 'ethnicity', and calculate the average unemployment rate of different geographic
    # regions
    average_unemployment_by_race = df_uk.groupby(['time', 'ethnicity'])['value'].mean().reset_index()
    # Pivot the table again to get the desired format with 'time' as the index
    average_unemployment_by_race = average_unemployment_by_race.pivot_table(index='time', columns='ethnicity',
                                                                            values='value')
    average_unemployment_by_race = average_unemployment_by_race.filter(
        items=['Asian', 'Black', 'White', 'Mixed', 'Other'])
    average_unemployment_by_race = average_unemployment_by_race.dropna(how='all')
    return average_unemployment_by_race


def process_oecd_education_data(df_oecd_education: pd.DataFrame) -> pd.DataFrame:
    """
    Adjusts the education level descriptions to a more generic classification and computes the average
    unemployment rates by these categories for European countries listed in a global list 'european_countries'.
    The DataFrame is then pivoted for easy visualization and analysis.

    Parameters:
    df_oecd_education (pd.DataFrame): A DataFrame containing columns 'Country', 'Education Level', and 'Value'
                                      where 'Value' typically represents an unemployment rate.

    Returns:
    pd.DataFrame: A DataFrame suitable for plotting that includes the country, remapped education levels, and
                  their corresponding average unemployment rates. The DataFrame is indexed by 'Country' and
                  'General Education Level'.

    DocTest:
    >>> data = {'Country': ['France', 'Germany', 'Spain', 'Italy'],
    ...         'Education Level': ['Doctoral or equivalent education', 'Upper secondary education',
    ...                             'Less than primary education', 'Master’s or equivalent education'],
    ...         'Value': [5, 15, 10, 8]}
    >>> df_oecd_education = pd.DataFrame(data)
    >>> processed_data = process_oecd_education_data(df_oecd_education)
    >>> processed_data
            Country                    Education Level  Unemployment Rate
    0    France                    Doctoral degree                5.0
    1   Germany                    Doctoral degree                NaN
    2     Italy                    Doctoral degree                NaN
    3     Spain                    Doctoral degree                NaN
    4    France  High school graduates, no college                NaN
    5   Germany  High school graduates, no college               15.0
    6     Italy  High school graduates, no college                NaN
    7     Spain  High school graduates, no college                NaN
    8    France    Less than a high school diploma                NaN
    9   Germany    Less than a high school diploma                NaN
    10    Italy    Less than a high school diploma                NaN
    11    Spain    Less than a high school diploma               10.0
    12   France                    Master's degree                NaN
    13  Germany                    Master's degree                NaN
    14    Italy                    Master's degree                8.0
    15    Spain                    Master's degree                NaN
    """
    df_oecd_education.rename(columns={'ISCED 2011 A education level': 'Education Level'}, inplace=True)
    # # Group the data by 'Country' and 'Education Level', to calculate the average unemployment rate over years
    # df_oecd_education = df_oecd_education.groupby(['Country', 'Education Level'])['Value'].mean().reset_index()
    # List of European countries according to the United Nations geoscheme for Europe.
    global european_countries
    # Filter out non-European countries
    df_oecd_education_europe = df_oecd_education[df_oecd_education['Country'].isin(european_countries)]
    # Reset index after filtering
    df_oecd_education_europe = df_oecd_education_europe.reset_index(drop=True)
    # Reference the global variable dictionary to map ISCED defined education levels to the generic education levels
    global isced_education_mapping
    # Apply the mapping to create a new 'General Education Level' column
    df_oecd_education_europe['General Education Level'] = df_oecd_education_europe['Education Level'].map(
        isced_education_mapping)
    # Group by the 'Country' and the new 'Generic Education Level' and calculate the mean of 'Value'
    df_oecd_education_grouped = \
        df_oecd_education_europe.groupby(['Country', 'General Education Level'], as_index=False)['Value'].mean()
    # Pivot the dataframe to reshape it for plotting
    pivot_df = df_oecd_education_grouped.pivot(index='Country', columns='General Education Level', values='Value')
    # Reset index to make 'Country' a column again
    pivot_df.reset_index(inplace=True)
    # Melt the DataFrame to have proper format for seaborn's barplot
    melted_df = pivot_df.melt(id_vars='Country', var_name='Education Level', value_name='Unemployment Rate')
    # Reference the education level order
    global education_level_order
    # Convert the 'Education Level' column to a categorical type with the specified order for better viewing
    melted_df['Education Level'] = pd.Categorical(
        melted_df['Education Level'],
        categories=education_level_order,
        ordered=True
    )
    return melted_df


def process_oecd_specific_countries(df_oecd: pd.DataFrame, countries: list):
    df_oecd.rename(columns={'ISCED 2011 A education level': 'Education Level', 'Value': 'Unemployment Rate'},
                   inplace=True)
    df_oecd_countries = df_oecd[df_oecd['Country'].isin(countries)][
        ['Country', 'YEAR', 'Education Level', 'Unemployment Rate']]

    # Reference the global variable dictionary to map ISCED defined education levels to the generic education levels
    global isced_education_mapping

    # Normalize the 'Education Level' values in the DataFrame and then map
    df_oecd_countries['General Education Level'] = df_oecd_countries['Education Level'].str.strip().map(
        isced_education_mapping)

    df_oecd_countries = df_oecd_countries.groupby(['Country', 'YEAR', 'General Education Level'])[
        'Unemployment Rate'].mean().reset_index()
    global education_level_order
    # Convert the 'Education Level' column to a categorical type with the specified order for better viewing
    df_oecd_countries['Education Level'] = pd.Categorical(
        df_oecd_countries['General Education Level'],
        categories=education_level_order,
        ordered=True
    )
    df_oecd_countries = df_oecd_countries.pivot(index=['Country', 'YEAR'], columns='Education Level',
                                                values='Unemployment Rate')
    return df_oecd_countries


def process_StatsGovCN_data(china_educated_year: pd.DataFrame, unemployment_file_path: str):
    china_educated_year = china_educated_year[
        ['year', 'province', '人均受教育年限']].rename(columns={'人均受教育年限': 'Average Educated Years'})
    china_national_educated_year = china_educated_year[china_educated_year['province'] == '全国'][
        ['year', 'Average Educated Years']]
    china_unemployment_rate = pd.read_excel(unemployment_file_path)[
        ['year', 'province', '城镇登记失业率(%)']].rename(columns={'城镇登记失业率(%)': 'Unemployment Rate'})
    china_national_unemployment_rate = china_unemployment_rate.groupby('year')['Unemployment Rate'].mean().reset_index()
    china_merged_df = china_national_educated_year.merge(china_national_unemployment_rate, how='inner',
                                                         on='year').set_index('year')
    return china_merged_df
