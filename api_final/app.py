from flask import Flask, render_template, jsonify, request
import csv

app = Flask(__name__)

CSV_ROWS = []
with open('Relatorio_cadop.csv', 'r', encoding='latin1') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=';')
    for row in csvreader:
        CSV_ROWS.append(row)

#Separar controller de funções auxiliares

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<term>')
def search(term):
    matching_rows = []
    for row in CSV_ROWS:
        for cell in row:
            if cell.find(term) == 1:
                matching_rows.append(row)
                break
    return render_template('index.html', results = matching_rows)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9001)