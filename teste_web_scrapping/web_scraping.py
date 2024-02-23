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
        return links
    html_plain_text = BeautifulSoup(page_content.content, 'html.parser')
    html_links = html_plain_text.find_all('a', class_='internal-link')
    # Adiciona ao dicionário <nome do arquivo>:<link>
    for link in html_links:
        href = link.get('href')
        filename = link.text
        links[filename] = href
    return links


def download_file(url: str, filename: str) -> None:
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)


def remove_files(files: list) -> None:
    for file in files:
        os.remove(file)


def zip_files(files: list, zip_filename: str) -> None:
    subprocess.run(["zip", zip_filename] + files, cwd="./")


def download_files(links: dict) -> list:
    downloaded_files = []
    for key, value in links.items():
        temp_split = str(value).split('.')
        extension = temp_split[-1]
        filename = f"{key}.{extension}"
        download_file(value, filename)
        downloaded_files.append(filename)
    return downloaded_files


def download_first_n_pdfs(links: dict, n: int) -> None:
    counter = 0
    for key, value in links.items():
        temp_split = str(value).split('.')
        extension = temp_split[-1]
        filename = f"{key}.{extension}"
        if extension == 'pdf' and counter < n:
            download_file(value, filename)
            counter += 1


def main():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    links = get_links(url)
    downloaded_files = download_files(links)
    zip_filename = "Anexos.zip"
    zip_files(downloaded_files, zip_filename)

    remove_files(downloaded_files)
    download_first_n_pdfs(links, 2)


if __name__ == "__main__":
    main()

