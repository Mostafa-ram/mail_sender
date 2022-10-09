from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

# read txt file that have emails / and parsing on it to get mails in List
with open("### put the file path here ###") as file:
    x = file.read()
single_mail = x.splitlines()

# take every mail in list and send cv to this mail
for i in single_mail:
    p = i.split()
    print(p)
    message = MIMEMultipart()
    message["from"] = "###put your name here###"
    message["to"] = p[0]
    message["subject"] = "### put your mail subject here ###"
    message.attach(MIMEText("""### put your body mail here ###"""))
    message.attach(MIMEImage(Path("### put cv path here ###").read_bytes()))

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()

        # here we log in with your mail and password
        smtp.login("### put your mail here ###", "### put your mail password here ###")
        x = 1

        # here we told the script to send the mail
        # you can repeat the mail as much as you  like by puting next line inside for loop
        smtp.send_message(message)
        print("sent ")
