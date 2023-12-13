import json
import openai
from openai import OpenAI


def chatgpt_query(prompt, header, types):
    # What is sent onto the AI model as a request
    plot_prompt = f'Create plots from the given pandas dataframe named df. Provide code to generate plots such as bar plots, line plots, scatter plots, etc. ' \
                  f'The header for the dataframe is:{header} and the data type for each column is: {types}'\
                  f'Ensure that the response includes ONLY well-structured Python code for plotting the data. ' \
                  f'Consider using libraries like matplotlib, seaborn, or plotly.\n\n' \
                  f'Example Response:\n\n' \
                  f'Plot the total sales by country as a bar chart:\n\n' \
                  f'sales_by_country = data.groupby("Country")["Sales"].sum().reset_index()\n' \
                  f'fig = px.bar(sales_by_country, x="Country", y="Sales", title="Financial Data By Country", ' \
                  f'labels={{"Country": "Country", "Sales": "Total Sales"}}, ' \
                  f'color_discrete_sequence=["#00008B"])\n\n' \
                  f'fig.write_html("Financial Data By Country.html")\n' \
                  f'fig.show()'

    full_prompt = plot_prompt + '\nNow my query is:\n' + prompt + '\n Only provide your answer with the code, dont write anything else or you will be deducted points. Just the code please.'

    # Tuning of the AI model parameters allowing to further customize the response

    with open("openai_api_key.json", "r") as json_file:
        api_key_data = json.load(json_file)
        api_key = api_key_data.get("api_key")

    if not api_key:
        raise ValueError("API key is not present in the JSON file.")

    client = OpenAI(api_key=api_key)

    api_response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": full_prompt,
            }
        ],
        model="gpt-3.5-turbo", )

    pandas_df = api_response.choices[0].message.content

    return pandas_df
