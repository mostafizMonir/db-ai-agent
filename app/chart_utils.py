import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io
import base64

def df_to_chart(df, chart_type='bar'):
    if df is None or df.empty:
        return None
    fig = None
    if chart_type == 'bar':
        fig = px.bar(df, x=df.columns[0], y=df.columns[1])
    elif chart_type == 'pie':
        fig = px.pie(df, names=df.columns[0], values=df.columns[1])
    if fig:
        return fig.to_html(full_html=False)
    return None