import os
import openai
from langchain.llms import OpenAI
from langchain.agents import Tool, initialize_agent, AgentType

llm = OpenAI(temperature=0)

def natural_language_to_sql(question, table_info):
    prompt = f"""
    Given the table schema: {table_info},
    Translate the question to a PostgreSQL SQL query:
    Question: {question}
    SQL:
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    sql_query = response['choices'][0]['message']['content'].strip()
    return sql_query