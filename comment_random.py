import requests
from bs4 import BeautifulSoup
import procesar_texto
import sortearpalabra

def link_first_entry(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    entry1 = soup.find_all('a', class_='comment-link')[0]
    return entry1.get('href')
    
def scrap_comments(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    comments = soup.find_all('p', class_='comment-content')
    text_end = ""
    for comment in comments:
        text_end = text_end + " " + comment.get_text()
    return text_end

def create_comment(url):
    go = link_first_entry(url)
    text_process = procesar_texto.cargar_texto(scrap_comments(go))
    return sortearpalabra.generar_texto(text_process[1],text_process,30)

