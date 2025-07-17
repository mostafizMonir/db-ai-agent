import streamlit as st
from db_utils import connect_to_db, run_query
from chart_utils import df_to_chart
from agent import natural_language_to_sql
import sqlalchemy

st.title("🧠 Agentic AI: Natural Language to SQL")

conn_str = st.text_input("Enter your DB connection string:", type="default")
question = st.text_area("Ask a question about your data:")
chart_type = st.selectbox("Chart Type (optional):", ["None", "bar", "pie"])

if st.button("Run") and conn_str and question:
    engine, conn = connect_to_db(conn_str)
    if not conn:
        st.error(f"DB Connection failed: {engine}")
    else:
        inspector = sqlalchemy.inspect(engine)
        tables = inspector.get_table_names()
        table_info = {}
        for table in tables:
            columns = inspector.get_columns(table)
            table_info[table] = [col['name'] for col in columns]

        sql_query = natural_language_to_sql(question, table_info)
        st.code(sql_query, language='sql')

        df = run_query(conn, sql_query)
        if df is not None:
            st.write(df)
            if chart_type != "None":
                html_chart = df_to_chart(df, chart_type)
                if html_chart:
                    st.components.v1.html(html_chart, height=500)
        else:
            st.error("Failed to run SQL query.")