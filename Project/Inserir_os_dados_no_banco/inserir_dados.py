from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import mysql.connector

dados_conexao = {"user":"root", "password":"", "host":"127.0.0.1", "database":"scrapyng_python"} #String de conexão
conexao = mysql.connector.connect(**dados_conexao) #Conector
cursor = conexao.cursor()

def inserir_dados_no_banco(titulo_informacao, url_informacao, conteudo_informacao):
    cursor.execute('INSERT INTO pagina_web (titulo_informacao, url_informacao, conteudo_informacao)'
                   'VALUES (%s, %s, %s)', (titulo_informacao, url_informacao, conteudo_informacao))
    conexao.commit()

def retirar_informacoes(site_de_informacao):
    url = site_de_informacao
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    titulo_da_noticia = bs.find('div', {'class': 'title'}).get_text()
    conteudo_da_noticia = bs.find('div', {'class':'mc-column content-text active-extra-styles'}).get_text()
    url_da_informacao = 'https://globoesporte.globo.com/futebol/times/palmeiras/noticia/palmeiras-define-inscritos-para-a-disputa-da-recopa-sul-americana-veja-a-lista.ghtml'
    inserir_dados_no_banco(titulo_da_noticia,url_da_informacao,conteudo_da_noticia)
    return 
retirar_informacoes("https://globoesporte.globo.com/futebol/times/palmeiras/noticia/palmeiras-define-inscritos-para-a-disputa-da-recopa-sul-americana-veja-a-lista.ghtml")



##REGEX FEITO PARA ENCONTRAR OS LINKS = (http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?