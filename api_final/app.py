from flask import Flask, render_template
import csv_processor as csv

app = Flask(__name__)

#Endpoint de pesquisa
@app.route('/search/<term>')
def search(term):
    matching_rows = csv.append_matching_rows(term)
    return render_template('result-list.html', results=matching_rows)

#Página inicial
@app.route('/')
def index():
    return render_template('index.html')

#Sobe o servidor
if __name__ == '__main__':
    csv.read_csv()
    app.run(host='0.0.0.0', port=9001)
    