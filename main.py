
import requests
TOKEN = "XXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
chat_id = "XXXXXXXXX"
text = " Hi, Im from CyberDefender Walkthrough :):) " #Send me sweet messege and I'll post it on my Twitter @milannshrestga:))

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"

r = requests.get(url)
print(r.json())




