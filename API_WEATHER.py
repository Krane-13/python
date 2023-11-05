import requests

API_KEY = "487516fbdc9c6aec9039e3a405bd5c1d"
cidade = "rolante"
link = "https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
# print(requisicao.json())

descricao= requisicao_dic['weather'][0]['description']
temperatura= requisicao_dic['main']['temp'] - 273.15

print(descricao, f"{temperatura}°C")