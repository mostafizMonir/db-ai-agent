import os
import openai
from langchain_openai  import OpenAI
from langchain.agents import Tool, initialize_agent, AgentType

llm = OpenAI(temperature=0)

# Initialize OpenAI client using the new API
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def natural_language_to_sql(question, table_info):
    prompt = f"""
    Given the table schema: {table_info},
    Translate the question to a PostgreSQL SQL query:
    Question: {question}
    SQL:
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    sql_query = response.choices[0].message.content.strip()
    return sql_query