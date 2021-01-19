import smtplib,ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email="sender_email@gmail.com"
receiver_email="receiver_email@gmail.com"
password = input("Enter your password")
message="""
subject: Hi there
 This message is sent from python."""
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message)