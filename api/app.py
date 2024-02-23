from flask import Flask, render_template
import csv_processor as csv

app = Flask(__name__)

#Endpoint de pesquisa que pode aceitar termos de pesquisa normais ou vazios
@app.route('/search/<term>')
@app.route('/search', defaults={'term': None})
def search(term: str):
    matching_rows = csv.append_matching_rows(term) if term else csv.append_all_rows()
    return render_template('result-list.html', results=matching_rows)

#Página inicial
@app.route('/')
def index():
    return render_template('index.html')


    