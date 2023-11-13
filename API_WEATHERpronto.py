import requests
import sqlite3

con= sqlite3.connect('BancoAPI.db')

API_KEY = "487516fbdc9c6aec9039e3a405bd5c1d"
cidade = "rolante"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

#link = "https://api.openweathermap.org/data/2.5/weather?q={" + cidade + "&appid={" + API_KEY +"}&lang=pt_br


requisicao = requests.get(link)
requisicao_dic = requisicao.json()
#print(requisicao_dic)

descricao= requisicao_dic['weather'][0]['description']
temperatura= requisicao_dic['main']['temp'] - 273.15

print(descricao, f"{temperatura:.2f}C")

cur=con.cursor()

try:
    cur.execute('''CREATE TABLE temp
    (descricao_temp, temperatura)''')
except:
    print ("tabela criada")
finally:
    cur.execute(f"insert into temp values ('{descricao}', '{temperatura:.2f}')")
    con.commit()
    con.close()
