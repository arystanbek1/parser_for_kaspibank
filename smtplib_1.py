import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
import os

email_sender = 'gulmirabakhytbekovna@gmail.com'
password = 'fqjmyryuohuhrjko'


smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(email_sender, password)


def send_mail(mail_mysql):
    msg = MIMEMultipart()
    msg.attach(MIMEText('Ваш парсинг файл'))
    with open("prices_from_kaspi_kz.xlsx", "rb") as f:
        file = MIMEApplication(f.read(), Name=basename("prices_from_kaspi_kz.xlsx"))
    msg.attach(file)
    email_getter = mail_mysql
    smtp_server.sendmail(email_sender, email_getter, msg.as_string())
    os.remove('prices_from_kaspi_kz.xlsx')