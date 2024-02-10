import csv

CSV_ROWS = []

#Lê o csv e guarda suas linhas numa lista
def read_csv() -> None:
    with open('Relatorio_cadop.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        for row in csvreader:
            CSV_ROWS.append(row)

#Retorna as linhas compatíveis com a pesquisa de texto
def append_matching_rows(term: str) -> list[str]:
    matching_rows = []
    term_upper = term.upper() 
    for row in CSV_ROWS:
        for cell_value in row.values():
            cell_value_upper = cell_value.upper()  
            if term_upper in cell_value_upper:
                matching_rows.append(row)
                break
    return matching_rows

def get_CSV_ROWS() -> list[str]:
    return CSV_ROWS