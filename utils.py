import pandas as pd
import os
import calendar


def read_excel_data(dir_path: str, file_name: str, blank_row: int):
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
        df = read_excel_data(dir_path, file, blank_row)
        df.reset_index(inplace=True)
        df['Month'] = df['Month'].map(month_to_num)
        df.set_index(['Year', 'Month'], inplace=True)
        if combined_df is None:
            combined_df = df
        else:
            combined_df = pd.merge(combined_df, df, left_index=True, right_index=True, how='left')
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