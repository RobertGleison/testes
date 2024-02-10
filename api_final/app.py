from flask import Flask, render_template
import csv

app = Flask(__name__)

#Lê o csv e guarda suas linhas numa lista
CSV_ROWS = []
with open('Relatorio_cadop.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=';')
    for row in csvreader:
        CSV_ROWS.append(row)

# def append_matching_rows():

@app.route('/search/<term>')
def search(term):
    matching_rows = []
    term_upper = term.upper() 
    for row in CSV_ROWS:
        for cell_value in row.values():
            cell_value_upper = cell_value.upper()  
            if term_upper in cell_value_upper:
                matching_rows.append(row)
                break
    return render_template('result-list.html', results=matching_rows)

#Página inicial
@app.route('/')
def index():
    return render_template('index.html')


#Sobe o servidor
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9001)