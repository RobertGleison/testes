from flask import render_template, Flask
from csv_reader import get_csv_rows
from server import app


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<term>')
def search(term):
    matching_rows = []
    term_upper = term.upper()  
    csv_rows = get_csv_rows()
    for row in csv_rows:
        for cell_value in row.values():
            cell_value_upper = cell_value.upper()  
            if term_upper in cell_value_upper:
                matching_rows.append(row)
                break
    return render_template('result-list.html', results=matching_rows)
