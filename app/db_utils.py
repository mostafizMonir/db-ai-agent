import sqlalchemy
import pandas as pd

def connect_to_db(conn_str):
    try:
        engine = sqlalchemy.create_engine(conn_str)
        connection = engine.connect()
        return engine, connection
    except Exception as e:
        return None, str(e)

def run_query(connection, query):
    try:
        df = pd.read_sql(query, connection)
        return df
    except Exception as e:
        return None
