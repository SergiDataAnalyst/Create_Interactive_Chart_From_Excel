import pandas as pd
import matplotlib as plt

from gpt_function import *

file = "Financial_Data.xlsx"

prompt = "I want to visualize a scatter plot of units sold vs gross sale"


def check_data_type(file):

    df = pd.read_excel(file, sheet_name="Data")
    headers = df.columns.tolist()
    row_index = 2
    row_data = df.iloc[row_index]

    column_type_list = []
    for column_name, value in row_data.items():
        data_type = type(value).__name__
        column_type = f"{column_name} is: {data_type}"
        column_type = str(column_type)
        column_type_list.append(column_type)

    return column_type_list, headers, df


column_types, headers, df = check_data_type(file)
print(column_types)
print(headers)

plot_query = chatgpt_query(prompt, headers, column_types)
print(plot_query)
exec(plot_query)



