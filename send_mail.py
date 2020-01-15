import smtplib

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "daddynexwave@gmail.com"
server = smtplib.SMTP(smtp_server,port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender_email, '741258963qwerty')
server.sendmail(sender_email,'daddynexwave@gmail.com','hello')
server.close()

