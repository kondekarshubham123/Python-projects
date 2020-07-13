import smtplib

to = input("Enter the email of recipent\n")

content = input("Compose mail\n")

def sendEMail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email','pass') # Replace email and pass with your email id and pass
    server.sendmail('email',to,content)
    server.close

sendEMail(to, content)
