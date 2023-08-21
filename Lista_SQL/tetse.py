import mysql.connector

con = mysql.connector.connect(host='127.0.0.1',  user='root', password='')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor Mysql versão ", db_info)
    curso = con.curso()
    curso.execute("select database();")
    linha = curso.fetchone()
    print("Conectado ao banco de dados", linha)

if con.is_connected():
    curso.close()
    con.close()
    print("Conexão ao Mysql foi encerrada")
