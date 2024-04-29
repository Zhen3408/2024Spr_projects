import main
import pandas as pd
import numpy as np


def df_transit(gdp_df)-> pd.DataFrame:
    """
    Transposes a DataFrame and sets the first row as new column headers after removing columns containing any NaN values.

    This function is specifically designed for GDP data where it is assumed that the first row after dropping NaN columns
    contains meaningful header information. The resulting DataFrame will have these headers with the corresponding transposed data.

    Parameters:
    gdp_df (pd.DataFrame): The input DataFrame containing GDP data with potential NaN values in any columns.

    Returns:
    pd.DataFrame: A transposed DataFrame with NaN-containing columns removed and the first row set as headers.

    unit test:
    >>> data = {'Year': [2020, 2021], 'GDP_US': [21000, None], 'GDP_UK': [2700, 2750]}
    >>> gdp_df = pd.DataFrame(data)
    >>> df_transit(gdp_df)
    Year    2020  2021
    GDP_UK  2700  2750
    """
    gdp_df_tp = gdp_df.dropna(axis=1).transpose()
    gdp_df_tp.columns = gdp_df_tp.iloc[0]
    gdp_df_tp = gdp_df_tp[1:]
    return gdp_df_tp



def process_unemployment_rate_df(unemployment_df)-> pd.DataFrame:
    """
    Processes a DataFrame containing unemployment rates. It renames a column, transposes the DataFrame,
    renames specified columns to standardized names, and resets the index.

    Parameters:
    unemployment_df (pd.DataFrame): The input DataFrame containing unemployment rate data with a column
                                    'Indicator Name' and potential NaN values in any columns.

    Returns:
    pd.DataFrame: A processed DataFrame with the index reset and the data restructured, having 'Year' as
                  one of the columns and renamed columns for male, female, and total unemployment rates.

    unit test:
    >>> data = {'Indicator Name': ['Unemployment, male (% of male labor force) (modeled ILO estimate)', 'Unemployment, female (% of female labor force) (modeled ILO estimate)', 'Unemployment, total (% of total labor force) (modeled ILO estimate)'], '2000': [None, None, 1.2] , '2001': [1.1, 1.2, 1.3], '2002': [5.5, 5.6,5.7],'2003': [5.2, 5.3,5.4]}
    >>> unemployment_df = pd.DataFrame(data)
    >>> process_unemployment_rate_df(unemployment_df)
    Year index male_rate female_rate total_rate
    0     2001       1.1         1.2        1.3
    1     2002       5.5         5.6        5.7
    2     2003       5.2         5.3        5.4
    """
    unemployment_df = unemployment_df.rename(columns={'Indicator Name': 'Year'})
    # transpose unemployment_df
    unemployment_df_tp = unemployment_df.dropna(axis=1).transpose()
    unemployment_df_tp.columns = unemployment_df_tp.iloc[0]
    unemployment_df_tp = unemployment_df_tp[1:]
    # rename the columns
    unemployment_df_tp = unemployment_df_tp.rename(columns={'Unemployment, male (% of male labor force) (modeled ILO estimate)':'male_rate',
                                           'Unemployment, female (% of female labor force) (modeled ILO estimate)':'female_rate',
                                           'Unemployment, total (% of total labor force) (modeled ILO estimate)':'total_rate'})
    
    unemployment_df_tp_reset = unemployment_df_tp.reset_index(drop=False)
    return unemployment_df_tp_reset



def read_and_process_yearly_unemp(df_unemp)-> pd.DataFrame:
    """
    Processes a DataFrame containing unemployment data by calculating the yearly average of unemployment.

    The function converts the 'Date' column to datetime, sets it as the index, and then resamples the data
    to calculate the annual mean. The result is a DataFrame with the 'Year' column and the annual average
    of the 'All workers' column.

    Parameters:
    df_unemp (pd.DataFrame): A DataFrame with a 'Date' column and an 'All workers' column containing
                             unemployment data.

    Returns:
    pd.DataFrame: A DataFrame with the index set to 'Year' and containing the yearly average unemployment
                  rates for 'All workers'.

    unit test:
    >>> data = {'Date': ['2020-01-01', '2020-12-31', '2021-01-01', '2021-12-31'],
    ...         'All workers': [5.0, 5.1, 5.5, 5.6]}
    >>> df_unemp = pd.DataFrame(data)
    >>> read_and_process_yearly_unemp(df_unemp)
       Year  All workers
    0  2020         5.05
    1  2021         5.55
    """
    df_unemp['Date'] = pd.to_datetime(df_unemp['Date'])
    df_unemp.set_index('Date', inplace=True)
    df_yearly_avg = df_unemp.resample('Y').mean()
    df_yearly_avg.reset_index(inplace=True)
    df_yearly_avg = df_yearly_avg.rename(columns={'Date': 'Year'})
    df_yearly_avg['Year'] = df_yearly_avg['Year'].dt.year
    df_yearly_avg = df_yearly_avg[['Year', 'All workers']]
    df_yearly_avg.set_index('Year')
    return df_yearly_avg




def process_state_population(df_state_population)-> pd.DataFrame:
    """
    Processes a DataFrame containing state population data by dropping unnecessary columns and renaming others.
    It filters the DataFrame to only include rows where the 'NAME' column matches one of the four specified regions.
    The columns are renamed to use the last four characters, which are assumed to be years.

    Parameters:
    df_state_population (pd.DataFrame): A DataFrame containing population data by state with columns for
                                        state information and years.

    Returns:
    pd.DataFrame: A processed DataFrame containing only population data for the four major regions of the
                  United States and with years as column headers.

    unit test:
    >>> data = {'SUMLEV': [40, 40], 'DIVISION': [1, 2], 'REGION': [3, 4], 'STATE': [5, 6], 'NAME': ['Northeast Region', 'West Region'], 'POPESTIMATE2010': [1000, 2000], 'POPESTIMATE2011': [500, 1500]}
    >>> df_state_population = pd.DataFrame(data)
    >>> process_state_population(df_state_population)
                 Region  2010  2011
    0  Northeast Region  1000   500
    1       West Region  2000  1500
    """
    df_state_population.drop(['SUMLEV','DIVISION','REGION','STATE'], axis=1, inplace=True)
    df_state_population.columns = [col[-4:] if len(col) > 4 else col for col in df_state_population.columns]
    df_state_population = df_state_population[(df_state_population['NAME'] == 'Northeast Region') | (df_state_population['NAME'] == 'Midwest Region') | (df_state_population['NAME'] == 'West Region') | (df_state_population['NAME'] == 'South Region')]
    df_state_population = df_state_population.rename(columns={'0POP' : '2009','NAME':'Region'})
    return df_state_population




def assign_division(state) -> str:
    """
    Assigns a US region division to a given state.

    This function categorizes each state into one of four regions: Midwest, Northeast, South, or West,
    based on predefined lists of states belonging to each region.

    Parameters:
    state (str): The name of the state to be categorized.

    Returns:
    str: A string representing the region to which the state belongs.

    unit test:
    >>> assign_division('Illinois')
    'Midwest Region'
    >>> assign_division('New York')
    'Northeast Region'
    """
    midwest = ['Iowa', 'Illinois', 'Indiana', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'North Dakota', 'Nebraska', 'Ohio', 'South Dakota', 'Wisconsin']
    northeast = ['Connecticut', 'Massachusetts', 'Maine', 'New Hampshire', 'New Jersey', 'New York', 'Pennsylvania', 'Rhode Island', 'Vermont']
    south = ['Alabama', 'Arkansas', 'District of Columbia', 'Delaware', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Maryland', 'Mississippi', 'North Carolina', 'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'West Virginia']
    west = ['Alaska', 'Arizona', 'California', 'Colorado', 'Hawaii', 'Idaho', 'Montana', 'New Mexico', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming']

    if state in midwest:
        return 'Midwest Region'
    elif state in northeast:
        return 'Northeast Region'
    elif state in south:
        return 'South Region'
    elif state in west:
        return 'West Region'


def process_eur_gdp(eur_gdp_df)-> pd.DataFrame:
    """
    Processes a DataFrame containing European GDP data. It removes unwanted columns, transposes the DataFrame,
    and then resets the index for the resulting DataFrame.

    The 'df_transit' function used in this process is assumed to be a pre-defined function which transposes a DataFrame
    and sets the first row as the new header. After transposing, it sets the columns to 'Year' and 'GDP'.

    Parameters:
    eur_gdp_df (pd.DataFrame): The input DataFrame containing GDP data with multiple columns,
                               where the necessary data is in the first and fifth columns.

    Returns:
    pd.DataFrame: A processed DataFrame with two columns: 'Year' and 'GDP', and the index reset.

    unit test:
    >>> data = {'Unnamed1': ['Country Name','European Union'], 'Unnamed2': ['Country Code', 'EU'], 'Unnamed3': ['Indicator Name', 'GDP (current US$)'],
    ...         'Unnamed4': ['Indicator Code', 'NY.GDP.MKTP.CD'], 'Unnamed5': ['1960', None], 'Unnamed6': ['1961', 15000000], 'Unnamed7': ['1962', 16000000]}
    >>> eur_gdp_df = pd.DataFrame(data)
    >>> process_eur_gdp(eur_gdp_df)
       Year       GDP
    0  1961  15000000
    1  1962  16000000
    """
    eur_gdp_df = eur_gdp_df.drop(eur_gdp_df.columns[[1, 2, 3]], axis=1)
    eur_gdp_df_tp = main.df_transit(eur_gdp_df)
    eur_gdp_df_tp.columns = ['Year', 'GDP']
    eur_gdp_df_tp = eur_gdp_df_tp.reset_index(drop=True)
    return eur_gdp_df_tp


def process_eur_unemp(eur_unemp_df)-> pd.DataFrame:
    """
    Processes a DataFrame containing European unemployment data. The function drops specific
    columns, transposes the DataFrame, assigns new headers, and resets the index.

    It uses a custom 'df_transit' function, assumed to be defined in the 'main' module, which
    transposes the DataFrame and sets the first row as new headers.

    Parameters:
    eur_unemp_df (pd.DataFrame): A DataFrame containing unemployment data with multiple columns,
                                    where the first column is country names and subsequent columns are years.

    Returns:
    pd.DataFrame: A processed DataFrame with two columns: 'Year' and 'Unemployment Rate',
                     with the index reset for easy access to the data.

    unit test:
    >>> data = {'Unnamed1': ['Country Name','European Union'], 'Unnamed2': ['Country Code', 'EU'], 'Unnamed3': ['Indicator Name', 'GDP (current US$)'],
    ...         'Unnamed4': ['Indicator Code', 'NY.GDP.MKTP.CD'], 'Unnamed5': ['1960', None], 'Unnamed6': ['1961', 8.92], 'Unnamed7': ['1962', 9.01]}
    >>> eur_gdp_df = pd.DataFrame(data)
    >>> process_eur_gdp(eur_gdp_df)
       Year   GDP
    0  1961  8.92
    1  1962  9.01
    """
    eur_unemp_df = eur_unemp_df.drop(eur_unemp_df.columns[[1, 2, 3]], axis=1)
    eur_unemp_df_tp = main.df_transit(eur_unemp_df)
    eur_unemp_df_tp.columns = ['Year', 'Unemployment Rate']
    eur_unemp_df_tp = eur_unemp_df_tp.reset_index(drop=True)
    return eur_unemp_df_tp

def get_USA_wage_data(min_wage_df)-> pd.DataFrame:
    """
    Extracts and transforms minimum wage data specifically for the United States from a given DataFrame.

    The function filters the data for the United States, transposes the DataFrame, and renames the columns
    to 'Year' and 'USA_wage'. The 'df_transit' function is assumed to be a previously defined function in the
    'main' module that transposes a DataFrame and sets the first row as the new header.

    Parameters:
    min_wage_df (pd.DataFrame): The input DataFrame containing minimum wage data with a 'Country' column.

    Returns:
    pd.DataFrame: A DataFrame with the 'Year' and 'USA_wage' columns representing the minimum wage data for
                  the United States over different years.

    unit test:
    >>> data = {'Country': ['United States', 'Belgium'], '1980': [3.18, 3.10], '1981': [3.35, 3.35]}
    >>> min_wage_df = pd.DataFrame(data)
    >>> get_USA_wage_data(min_wage_df)
       Year USA_wage
    0  1980     3.18
    1  1981     3.35
    """
    USA_min_wage_df = min_wage_df[min_wage_df['Country'] == 'United States']
    USA_min_wage_df = main.df_transit(USA_min_wage_df)
    USA_min_wage_df = pd.DataFrame(USA_min_wage_df).reset_index()
    USA_min_wage_df.columns = ['Year', 'USA_wage']
    return USA_min_wage_df




def calculate_eur_wage_avg(min_wage_df)-> pd.DataFrame:
    """
    Calculates the average minimum wage across European countries from a given DataFrame.

    This function copies the input DataFrame, replaces placeholders for missing data ('..') with NA values,
    drops all rows with missing values, then calculates the mean for each year and returns a new DataFrame
    with these average values.

    Parameters:
    min_wage_df (pd.DataFrame): The input DataFrame containing minimum wage data for multiple countries
                                with a 'Country' column and year columns.

    Returns:
    pd.DataFrame: A DataFrame with 'Year' and 'eur_wage' columns representing the average minimum wage for
                  European countries by year.

    unit test:
    >>> data = {'Country': ['France', 'Germany', 'Italy'], '2010': [9.00, 8.50, pd.NA], '2011': [9.10, 8.60, 8.00]}
    >>> min_wage_df = pd.DataFrame(data)
    >>> calculate_eur_wage_avg(min_wage_df)
       Year eur_wage
    0  2010     8.75
    1  2011     8.85
    """
    eur_min_wage_df = min_wage_df.copy()
    eur_min_wage_df.replace('..', pd.NA, inplace=True)
    eur_min_wage_df.dropna(inplace=True)
    average_values = eur_min_wage_df.loc[:, eur_min_wage_df.columns != 'Country'].mean()
    averages_df = pd.DataFrame(average_values).reset_index()
    averages_df.columns = ['Year', 'eur_wage'] 
    return averages_df



def calculate_GDP_Growth(gdp_df_tp_reset)-> pd.DataFrame:
    """
    Calculates the annual GDP growth rate based on the given DataFrame.

    The function computes the year-over-year GDP growth percentage using the formula:
    [(Current Year GDP - Previous Year GDP) / Previous Year GDP] * 100

    Parameters:
    gdp_df_tp_reset (pd.DataFrame): The input DataFrame containing a 'GDP' column with GDP values
                                    for consecutive years.

    Returns:
    pd.DataFrame: The input DataFrame is returned with an additional 'GDP_Growth' column representing
                  the annual GDP growth rate.

    unit test:
    >>> data = {'Year': [2018, 2019, 2020], 'GDP': [2000, 2100, 2200]}
    >>> gdp_df_tp_reset = pd.DataFrame(data)
    >>> calculate_GDP_Growth(gdp_df_tp_reset)
       Year   GDP  GDP_Growth
    0  2018  2000         NaN
    1  2019  2100    5.000000
    2  2020  2200    4.761905
    """
    gdp_df_tp_reset['GDP_Growth'] = ((gdp_df_tp_reset['GDP'] - gdp_df_tp_reset['GDP'].shift(1)) / gdp_df_tp_reset['GDP'].shift(1)) * 100
    return gdp_df_tp_reset



def calculate_Population_Growth(df_state_unemp_pop_reg)-> pd.DataFrame:
    """
    Calculates the population growth rate for each region within a DataFrame.

    The function first adjusts the population data by multiplying by 10^7 to convert data to an appropriate scale.
    Then, it computes the year-over-year population growth percentage by region using the formula:
    [(Current Year Population - Previous Year Population) / Previous Year Population] * 100.

    Parameters:
    df_state_unemp_pop_reg (pd.DataFrame): A DataFrame that includes 'Population' and 'Region' columns, where
                                           'Population' is in units that need to be scaled by 10^7, and 'Region'
                                           indicates the region each row of data belongs to.

    Returns:
    pd.DataFrame: The original DataFrame with an additional 'Population_Growth' column representing the
                  annual population growth rate for each region.

    unit test:
    >>> data = {'Region': ['Midwest Region', 'Midwest Region', 'West Region', 'West Region'], 'Year': [2018, 2019, 2018, 2019], 'Population': [0.683, 0.686, 0.780, 0.784]}
    >>> df_state_unemp_pop_reg = pd.DataFrame(data)
    >>> calculate_Population_Growth(df_state_unemp_pop_reg)
               Region  Year  Population  Population_Growth
    0  Midwest Region  2018   6830000.0                NaN
    1  Midwest Region  2019   6860000.0           0.439239
    2     West Region  2018   7800000.0                NaN
    3     West Region  2019   7840000.0           0.512821
    """
    df_state_unemp_pop_reg['Population'] = df_state_unemp_pop_reg['Population'] * 10**7
    df_state_unemp_pop_reg['Population_Growth'] = df_state_unemp_pop_reg.groupby('Region')['Population'].transform(lambda x: x.pct_change()) * 100
    return df_state_unemp_pop_reg



def calculate_EU_population_growth(euro_merged_df) -> pd.DataFrame:
    """
    Calculates the year-over-year population growth percentage for a DataFrame containing European population data.

    The function computes the population growth percentage by taking the percentage change between consecutive years
    in the 'Population' column.

    Parameters:
    euro_merged_df (pd.DataFrame): The input DataFrame containing a 'Population' column with numerical values
                                   representing the population for consecutive years.

    Returns:
    pd.DataFrame: The same DataFrame with an additional 'Population_Growth' column representing the annual
                  population growth percentage.

    unit test:
    >>> data = {'Year': [2018, 2019, 2020], 'Population': [50000000, 50500000, 51000000]}
    >>> euro_merged_df = pd.DataFrame(data)
    >>> calculate_EU_population_growth(euro_merged_df)
       Year  Population  Population_Growth
    0  2018    50000000                NaN
    1  2019    50500000           1.000000
    2  2020    51000000           0.990099
    """
    euro_merged_df['Population_Growth'] = euro_merged_df['Population'].pct_change() * 100
    return euro_merged_df



def calculate_EU_GDP_Growth(euro_merged_df)-> pd.DataFrame:
    """
    Calculates the year-over-year GDP growth percentage for a DataFrame containing European GDP data.

    This function computes the GDP growth rate by taking the percentage change between consecutive years
    in the 'GDP' column. The result is expressed as a percentage to facilitate economic analysis and reporting.

    Parameters:
    euro_merged_df (pd.DataFrame): The input DataFrame containing 'GDP' column with numerical values representing
                                   the GDP for consecutive years.

    Returns:
    pd.DataFrame: The same DataFrame with an additional 'GDP_Growth' column representing the annual GDP growth
                  percentage.

    unit test:
    >>> data = {'Year': [2018, 2019, 2020], 'GDP': [1.8e12, 1.85e12, 1.9e12]}
    >>> euro_merged_df = pd.DataFrame(data)
    >>> calculate_EU_GDP_Growth(euro_merged_df)
       Year           GDP  GDP_Growth
    0  2018  1.800000e+12         NaN
    1  2019  1.850000e+12    2.777778
    2  2020  1.900000e+12    2.702703
    """
    euro_merged_df['GDP_Growth'] = euro_merged_df['GDP'].pct_change() * 100
    return euro_merged_df