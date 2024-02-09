import tabula
import pandas as pd
import zipfile
import os
import logging


#Para que possam rodar este arquivo, é necessário ter instalado o Java.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Leitura do pdf utilizando um template.json com as coordenadas da tabela na página correspondente
def extraction(pdf: str, template: str) -> list[any]:
    try:
        logger.info(f" Iniciado extração de dados")
        data = tabula.read_pdf_with_template(
        pdf,
        template,
        pandas_options={'header': None} # Evita que a primeira linha com dados do arquivo vire um cabeçalho de tabela
    )  
    except:
        logger.info(f" Extração de tabela incompleta. Insira um arquivo e um template compatíveis.")
        return[]
    logger.info(f" Anexo lido com sucesso. Iniciando a extração da tabela.")
    return data

def create_csv(data: list[any]) -> str:
    column_names = ["PROCEDIMENTO", "RN (alteração)", "VIGÊNCIA", "Seg.Odontológica", "Seg.Ambiental", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"]
    merged_csv = pd.concat([table for table in data], ignore_index=True) # Concatena as tabelas
    merged_csv.columns = column_names # Atribui column_names como cabeçalho
    csv_filename = "rol_de_procedimentos.csv"
    merged_csv.to_csv(csv_filename, index=False)
    logger.info(f" Arquivo CSV '{csv_filename}' criado com sucesso.")
    return csv_filename

def create_zip(csv_name: str) -> None:
    zip_filename = "Teste_Robert_Gleison_dos_Reis_Pereira.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(csv_name, os.path.basename(csv_name))
    #Remove os .csv fora do zip
    os.remove(csv_name)


data = extraction("anexo1.pdf", "anexo1.tabula-template.json")
csv_name = create_csv(data)
create_zip(csv_name)