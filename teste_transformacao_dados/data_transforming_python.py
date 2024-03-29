import csv

import tabula
import zipfile
import os
import logging
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Leitura do pdf utilizando um template.json com as coordenadas da tabela na página correspondente
def extraction(pdf: str, template: str) -> list[any]:
    try:
        logger.info(f" Iniciado extração de dados")
        data = tabula.read_pdf_with_template(
            pdf,
            template,
            pandas_options={'header': None}
            # Evita que a primeira linha com dados do arquivo vire um cabeçalho de tabela
        )
    except:
        logger.info(f" Extração de tabela incompleta. Insira um arquivo e um template compatíveis.")
        return []
    logger.info(f" Anexo lido com sucesso. Iniciando a extração da tabela.")
    return data


def create_csv(data: list[any]) -> str:
    merged_data = []
    csv_filename = "rol_de_procedimentos.csv"
    column_names = ["PROCEDIMENTO", "RN (alteração)", "VIGÊNCIA", "Seg.Odontológica", "Seg.Ambiental", "HCO", "HSO",
                    "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"]

    # Transforma a lista de dataframes em uma lista de tuplas com 13 colunas
    for df in data:
        df.replace(np.nan, '', inplace=True)
        temp_list = df.to_records(index=False).tolist()
        merged_data += temp_list

    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(column_names)
        for row in merged_data:
            writer.writerow(row)

    return csv_filename


def create_zip(csv_name: str) -> None:
    zip_filename = "Teste_Robert_Gleison_dos_Reis_Pereira.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(csv_name, os.path.basename(csv_name))
    # Remove os .csv fora do zip
    os.remove(csv_name)

def main():
    data = extraction("anexo1.pdf", "template_final.json")
    csv_name = create_csv(data)
    create_zip(csv_name)


if __name__ == "__main__":
    main()