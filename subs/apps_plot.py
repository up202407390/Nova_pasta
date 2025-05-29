from flask import render_template, session
from classes.Book import Book
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import io
import base64

def apps_plot():
    # Creates a pandas dataframe with the orderproduct table data
    engine = create_engine('sqlite:///' + filename + 'library.db')
    df_Book = pd.read_sql_query('SELECT * FROM Book', con=engine)

    # Uses groupby to obtain the total quantity order by product id
    result = df_Book.groupby('genre').size()
   
    genres = result.index.tolist()
    counts = result.values
    
    # Uses matplotlib to draw a bar chart
    fig, ax = plt.subplots()
    ax.bar(genres, counts, color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Género')
    plt.ylabel('Número de Livros')
    plt.title('Quantidade de Livros por Género')
    
    # Save plot to a bytes buffer
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image = base64.b64encode(buf.getvalue()).decode('utf-8')

    return render_template("plot.html", image=image, ulogin=session.get("user"))