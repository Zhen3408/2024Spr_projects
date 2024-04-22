import pandas as pd
import os


def read_excel_data(dir_path, file_name):
    # Construct the full file path
    full_path = os.path.join(dir_path, file_name)
    # Read the excel file
    df = pd.read_excel(full_path, skiprows=11)

    month_column = df.columns.tolist()
    month_column.remove('Year')
    age_header = file_name.split('.')[0]

    # Restructure the data frame, unpivot the data, set year and month as index
    df = pd.melt(df, id_vars='Year', value_vars=month_column, var_name='Month', value_name=age_header)
    df.set_index(['Year', 'Month'])
    return df
