from flask import render_template, session
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px

def apps_plotly():
    # Conecta ao banco da biblioteca
    engine = create_engine('sqlite:///data/library.db')
    df_book = pd.read_sql_query('SELECT * FROM Book', con=engine)


    # Agrupa por género e conta o número de livros por género
    result = df_book.groupby('genre').size()

    genres = result.index.tolist()
    counts = result.values

    # Cria gráfico interativo com Plotly
    fig = px.bar(
        x=genres,
        y=counts,
        labels={'x': 'Género', 'y': 'Número de Livros'},
        title='Número de Livros por Género',
        color=counts,  # Para dar cor de acordo com a quantidade
        color_continuous_scale='Blues'
    )

    plot_div = fig.to_html(full_html=False, div_id='my-plot')

    return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"))
