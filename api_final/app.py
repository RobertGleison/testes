from flask import Flask, render_template
import csv_processor as csv

app = Flask(__name__)

#Endpoint de pesquisa que pode aceitar termos de pesquisa normais ou vazios
@app.route('/search', defaults={'term': None})
@app.route('/search/<term>')
def search(term):
    if term:
        matching_rows = csv.append_matching_rows(term)
    else:
        matching_rows = csv.append_all_rows()
    return render_template('result-list.html', results=matching_rows)


#Página inicial
@app.route('/')
def index():
    return render_template('index.html')

#Sobe o servidor
if __name__ == '__main__':
    csv.read_csv()
    app.run(host='0.0.0.0', port=9001)
    