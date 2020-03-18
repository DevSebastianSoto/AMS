import os
import json
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'web.messenger.ams@gmail.com'
EMAIL_PASSWORD = 'vmmrgawxvzzwvbft'


def readJson(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def sendMail(name, email, subject, msg):
    mail = EmailMessage()
    mail['Subject'] = subject
    mail['From'] = EMAIL_ADDRESS
    mail['To'] = EMAIL_ADDRESS
    mail.set_content(f'{name}:\t{email}\n\n{msg}')
    mail.add_alternative(f"""
                            <!DOCTYPE html>
                            <html lang="en">

                            <body>
                                <div style="margin: 1rem; ">
                                    <div style="text-decoration: none; text-align: center; line-height: 1.15rem; margin-bottom: 1rem;">
                                        <h1 style="text-transform: capitalize; margin: 0px">{name}</h1>
                                        <h3 style=" margin: 10px">{email}</h3>
                                    </div>
                                    <div style="padding: 0.5rem; border: 1px solid rgba(100,100,100,0.5);">
                                        <p style="margin: 0px; padding: 1rem;">{msg}</p>
                                    </div>
                                </div>
                            </body>

                            </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(mail)
