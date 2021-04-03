import mysql.connector

minha_conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database="scrapyng_python")
cursor = minha_conexao.cursor()

consultar_dados_do_banco = ('SELECT titulo_informacao, url_informacao, conteudo_informacao FROM pagina_web')

cursor.execute(consultar_dados_do_banco)

for (titulo_informacao, url_informacao, conteudo_informacao) in cursor:
    print(f'Título: {titulo_informacao}, URL: {url_informacao}, Conteúdo: {conteudo_informacao}')
cursor.close()
minha_conexao.close()