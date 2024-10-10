import requests
import json
from datetime import datetime, timedelta

url = "https://www.niftyindices.com/Backpage.aspx/getHistoricaldataDBtoString"


end_date = datetime.today().strftime('%d-%b-%Y')
start_date = (datetime.today() - timedelta(days=7)).strftime('%d-%b-%Y')

nifty50 = {
    'name': 'Nifty 50',
    'startDate': start_date,
    'endDate': end_date
}

Nifty500Momentum50  = {
    'name': 'Nifty500 Momentum 50',
    'startDate': start_date,
    'endDate': end_date
}

Nifty200Momentm30 = {
    'name': 'Nifty200Momentm30',
    'startDate': start_date,
    'endDate': end_date
}

NIFTY100LOWVOL30 = {
    'name': 'NIFTY100 LOWVOL30',
    'startDate': start_date,
    'endDate': end_date
}

NIFTY100LOWVOL30 = {
    'name': 'NIFTY100 LOWVOL30',
    'startDate': start_date,
    'endDate': end_date
}


NiftyMidcap150Momentum50 = {
    'name': 'Nifty Midcap150 Momentum 50',
    'startDate': start_date,
    'endDate': end_date
}

headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.niftyindices.com'
}

def send_slack_notification(message, webhook_url):
    payload = {
        "text": message
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")


indices  =  [nifty50, NIFTY100LOWVOL30, Nifty200Momentm30, Nifty500Momentum50, NiftyMidcap150Momentum50]

# print("from: ", start_date, "to: ", end_date)
returns = []
send = []

for index in indices:
    r = requests.post(url, json=index, headers=headers)
    output = json.loads(r.text)
    returns.append(output['d'].split('[')[0].strip())
    send.append(f"{index['name']} : {output['d'].split('[')[0].strip()}")
    # print(index['name'], ":", output['d'].split('[')[0].strip())

slack_webhook_url = "https://hooks.slack.com/services/XXXXXXXXXXX/" # modifty this with your slack webhook

if all(float(rn) < 0 for rn in returns):
    message = f"INVEST!! INVEST!! INVEST!! \nAll negatives!! from: {start_date} to: {end_date} \n{'\n'.join(send)}"
    send_slack_notification(message, slack_webhook_url)
# else:
#     message = f"Don't Invest!! Not negative!! \n{'\n'.join(send)}"
#     send_slack_notification(message, slack_webhook_url)



# input()