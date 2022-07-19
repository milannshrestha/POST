
import requests
TOKEN = "XXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
chat_id = "XXXXXXXXX"
text = "YOUR MSG HERE) "

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"

r = requests.get(url)
print(r.json())




