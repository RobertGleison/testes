import csv

CSV_ROWS = []

def read_csv():
    global CSV_ROWS
    with open('Relatorio_cadop.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        for row in csvreader:
            CSV_ROWS.append(row)

def get_csv_rows():
    if not CSV_ROWS:
        read_csv()
    return CSV_ROWS
