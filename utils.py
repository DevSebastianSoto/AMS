import os
import json
import smtplib

EMAIL_ADDRESS = 'dev.snsm@gmail.com'
EMAIL_PASSWORD = 'xluixaleqegxonuh'

def readJson(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def sendMail(email, first_name, last_name, msg):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        msg = f'Subject: {first_name} {last_name}\n\n{msg}'
        smtp.sendmail(email, EMAIL_ADDRESS, msg)