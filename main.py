
import requests
TOKEN = "XXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
chat_id = "XXXXXXXXX"
text = " Hi, Im from CyberDefender Walkthrough :):) " #Send me a sweet messege if you use this script, :))

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"

r = requests.get(url)
print(r.json())




