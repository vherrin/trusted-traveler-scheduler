# https://www.lifewire.com/how-to-email-a-text-4147467   This has the if
# this will send an email that will inturn send a text message to your phone

import smtplib
from email.mime.text import MIMEText
from .config import Config


def send_email(config, message):
    msg = MIMEText(message)
    msg['Subject'] = config.email_subject
    msg['From'] = config.email_from 
    msg['To'] = config.email_to
    debuglevel = True
    mail = smtplib.SMTP(config.smtp_server, config.smtp_port)
    mail.set_debuglevel(debuglevel)
    mail.starttls()
    mail.login(config.smtp_username, config.smtp_password)
    mail.sendmail(config.email_from, config.email_to, msg.as_string())
    mail.quit()
    
    


