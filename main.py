import requests
from bs4 import BeautifulSoup
from output import Output
from mail import check_mail
import json


with open("userdata.json", 'r') as file:
    user_data = json.load(file)
# import os
# os._exit(0)

payload = {
    'division': 'senior',
    'rdo': '1',
    'Loginid': user_data['user'],
    'LoginPwd': user_data['password'],
    'Uid': ''
}

s = requests.Session()
result = s.post(user_data['login_url'], data=payload)
res2 = s.get(user_data['load_url'])
soup = BeautifulSoup(res2.text, features="html.parser")
table_tag = soup.find('table', {'id': 'Table1'})
tr_tags = table_tag.select('tr')
words = []
for tag in tr_tags:
    words.extend(tag.text.split())

words = Output(words)
# print(words)
havencomeout = {}

i = 3
while i < len(words):
    havencomeout[words[i]] = 1
    if words[i+1] == '缺':
        # print(words[i] + 'haven\' come out.')
        havencomeout[words[i]] = 0
    i += 3

# print(havencomeout)

# check_mail(havencomeout)
