import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "****@gmail.com"
toaddr = "****@gmail.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Enetcom ATTENDACE SYSTEM"
body = "Alert code 307 : stranger try to enter the system "
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()  # Establish connection
server.starttls()  # Enable TLS
server.ehlo()  # Re-establish connection
server.login(fromaddr, "xxxx xxxx xxxx ")  # Authenticate
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()