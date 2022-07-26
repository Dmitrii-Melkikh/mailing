# sender = "melkih.db@gmail.com"
# password = "04062002Mm"
#
# server = smtplib.SMTP("smtp.gmail.com",587)
# server.ehlo()
# server.starttls()
# message = 'Hello!'
# try:
#     server.login(sender,password)
#     server.sendmail(sender, sender, message)
# except Exception as _ex:
#     print(f"{_ex}\nCheck your login or password please!")

import smtplib
import info
from email.mime.text import MIMEText

def ya_sending(email_text,dest_email):
    email = info.ya_login
    password = info.ya_password

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)

    dest_email = dest_email
    subject = 'Booking from chatbot'
    email_text = MIMEText(email_text)
    email_text["Subject"] = "Это Тема"
    email_text["From"] = email
    email_text["To"] = dest_email
    server.set_debuglevel(1) # Необязательно; так будут отображаться данные с сервера в консоли
    server.sendmail(email, dest_email, email_text.as_string())
    server.quit()


def main():
    mail = input("Choose your email:\n1 - yandex\n2 - gmail\n3 - mail\n")
    text_message = input("Enter text of message: ")
    dest_addr = input("Destination adress: ")
    if mail == '1':
        ya_sending(text_message,dest_addr)

if __name__ == "__main__":
    main()