import smtplib
import json

filename = 'haven_come_out.json'

email_account = 'bobwang507@gmail.com'
email_password = 'bob32174129'
subjects = {
    '地理': 'Geography',
    '基礎化學': 'Chemistry',
    '基礎物理': 'Physical',
    '數學': 'Mathematics',
    '歷史': 'History',
    '英文': 'English',
    '選修地科': 'Geoscience'
}


def check_mail(aft_havencomeout):
    with open(filename, 'r') as file:
        bef_havencomeout = json.load(file)
    for key, value in bef_havencomeout.items():
        if(aft_havencomeout[key] != value):
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.starttls()
            smtpObj.login(email_account, email_password)  # 第一個參數是電郵帳號，第二個參數是密碼
            to = [email_account]  # 收件者的電郵地址，為list資料型態
            msg = subjects[key] + ' CAME OUT!'  # 電子郵件內文

            smtpObj.sendmail(email_account, to, msg)  # 利用sendmail 這個method 來寄出電郵，SMTP.sendmail(from_addr, to_addrs, msg, mail_options=[], rcpt_options=[])
            smtpObj.quit()  # 關閉本地端對遠端郵件伺服器的連線
    with open(filename, 'w') as file:
        json.dump(aft_havencomeout, file)
