from bs4 import BeautifulSoup
import os
import requests
import subprocess

def get_links(url: str) -> dict:
    links = {}
    try:
        page_content = requests.get(url)
    except requests.exceptions.RequestException:
        print(f"Error accessing the URL {url}, please insert a valid one.")

    html_plain_text = BeautifulSoup(page_content.content, 'html.parser')
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

def main():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    links = get_links(url)
    zip_all_files(links)
    download_first_and_second_pdf(links)

if __name__ == "__main__":
    main()