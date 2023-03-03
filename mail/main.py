import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


server = smtplib.SMTP("smtp.gmail.com",9000)
server.ehlo()

server.login("haneel.j.777@gmail.com","Bjul31997@")

server.sendmail("haneel.j.777@gmail.com","illusin321@gmail.com","Hi Haneel Kumar Nagineni")