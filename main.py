
import requests
TOKEN = "XXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
chat_id = "XXXXXXXXX"
text = " Hi, Im from CyberDefender Walkthrough :):) " # Let me know where you came from :)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"

r = requests.get(url)
print(r.json())




