from flask import Flask, render_template, jsonify, request
import csv

app = Flask(__name__)

CSV_ROWS = []
with open('Relatorio_cadop.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=';')
    for row in csvreader:
        CSV_ROWS.append(row)

for i in CSV_ROWS:
    print(i)

#Separar controller de funções auxiliares

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<term>')
def search(term):
    matching_rows = []
    term_upper = term.upper()  # Convert term to uppercase
    for row in CSV_ROWS:
        for cell_value in row.values():
            cell_value_upper = cell_value.upper()  # Convert cell_value to uppercase
            if term_upper in cell_value_upper:
                matching_rows.append(row)
                break
    return render_template('result-list.html', results=matching_rows)



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9001)