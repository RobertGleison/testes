import csv

CSV_ROWS = []

#Lê o csv e guarda suas linhas numa lista
def read_csv() -> None:
    try:
        with open('Relatorio_cadop.csv', 'r', encoding='utf-8') as csvfile:
            #Guarda as linhas em forma de dicionário, 'coluna': linha
            csvreader = csv.DictReader(csvfile, delimiter=';')
            for row in csvreader:
                CSV_ROWS.append(row)
    except RuntimeError:
        print("Error in reading the csv file.")

#Retorna as linhas do CSV compatíveis com a pesquisa de texto
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

#Retorna todas as linhas do CSV
def append_all_rows() -> list[str]:
    matching_rows = []
    for row in CSV_ROWS:
        matching_rows.append(row)
    return matching_rows


def get_CSV_ROWS() -> list[str]:
    return CSV_ROWS