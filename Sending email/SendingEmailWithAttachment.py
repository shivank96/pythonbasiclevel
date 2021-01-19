import email,smtplib,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with Attachment from python"
body = "This is an email with attachment"
sender_mail = "Sender_mail@gmail.com"
receiver_email = "receiver_mail@gmail.com"
password = input("Enter your password")

message = MIMEMultipart()
message["From"]=sender_mail
message["To"]=receiver_email
message["subject"]=subject
message["Bcc"]=receiver_email

message.attach(MIMEText(body,'plain'))

filename = "any file.extension of it"

with open(filename,"rb") as attachment:
    part = MIMEBase("appllication","octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition",f"attachment; filename={filename}",)
message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_mail,password,)
    server.sendmail(sender_mail,receiver_email,text)

