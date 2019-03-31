import requests
from bs4 import BeautifulSoup
from output import Output
from mail import check_mail

login_url = 'http://schoolsys.wlsh.tyc.edu.tw/online/login.asp'
user = '610030'
password = 'E125814309'
filename = 'out.txt'

payload = {
    'division': 'senior',
    'rdo': '1',
    'Loginid': user,
    'LoginPwd': password,
    'Uid': ''
}

s = requests.Session()
result = s.post(login_url, data=payload)
res2 = s.get('http://schoolsys.wlsh.tyc.edu.tw/online/selection_student/student\
_subjects_number.asp?action=%A6U%A6%A1%A6%A8%C1Z&thisyear=107&thisterm=2&nu\
mber=7201&exam_name=107%282%29%B2%C4%A4%40%A6%B8%ACq%A6%D2%02')
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

check_mail(havencomeout)
