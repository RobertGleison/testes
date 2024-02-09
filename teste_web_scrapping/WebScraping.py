from bs4 import BeautifulSoup
import os
import requests
import subprocess

'''
Necessário instalar o pacote BeautifulSoup e Requests. Podem ser baixados com os seguintes comandos:
pip install requests
pip install beautifulsoup4

Documentação do BeautifulSoup, usado como referência:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all
'''


def get_links(url: str) -> dict:
    links = {}
    try:
        page_content = requests.get(url)
    except requests.exceptions.RequestException:
        print("Error accessing the URL, please insert a valid one.")

    # Transforma a página em um texto plano baseado em html
    html_plain_text = BeautifulSoup(page_content.content, 'html.parser')
    # Encontra todas as tags <a></a> com a classe 'internal-link'
    html_links = html_plain_text.find_all('a', class_='internal-link')

    #Adiciona ao dicionário <nome do arquivo>:<link>
    for link in html_links:
        href = link.get('href')
        filename = link.text
        links[filename] = href

    return links


def download_first_and_second_pdf(links: dict) -> None:
    counter = 0
    for key, value in links.items():
        if value.endswith('.pdf') and counter < 2:
            counter += 1
            subprocess.run(["curl", "-o", key + '.pdf', value], cwd="./")


def zip_all_files(links: dict) -> None:
    zip_filename = "Anexos.zip"
    for key, value in links.items():
        temp_split = str(value).split('.')
        #Pega a extensão do arquivo para renomeá-lo
        extension = temp_split[-1]
        subprocess.run(["curl", "-o", f"{key}.{extension}", value], cwd="./")
    downloaded_files = [f"{key}.{value.split('.')[-1]}" for key, value in links.items()]
    subprocess.run(["zip", zip_filename] + downloaded_files, cwd="./")

    #Remove os arquivos baixados fora do arquivo .zip
    for file in downloaded_files:
        os.remove(file)


url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
zip_all_files(get_links(url))
download_first_and_second_pdf(get_links(url))
