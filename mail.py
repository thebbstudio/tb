import smtplib
from email.mime.text import MIMEText
import conf


def send_email(data):
    sender = conf.sender
    password = conf.password
    receiver = conf.receiver

    text = 'Имя и город: ' + str(data[1]) \
           + '\nКонтактная информация: ' + str(data[3]) \
           + '\nОписание: ' + str(data[2]) \
           + '\nМаркет плайс: ' + str(data[4]) + '\n'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    print(text)
    msg = MIMEText(text)

    msg['Subject'] = 'Данные о клиентах от бота'
    msg['From'] = sender
    msg['To'] = receiver

    server.ehlo()
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string().encode('utf-8'))
        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

