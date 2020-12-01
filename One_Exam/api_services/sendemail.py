import configparser
import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random, string

import sys, os, django
sys.path.append('D:\projects\pocs\poc')
os.environ['DJANGO_SETTINGS_MODULE'] = 'poc.settings'
django.setup()

from backend.models import Participant, Paper_Instance

config = configparser.ConfigParser()
config.read(os.environ['OneExamCONFIG'] + '/config.ini')
email_config = config['SEND_EMAIL_CONFIG']


def sendEmail():
    try:
        participants = Participant.objects.all()
        for participant in participants:
            email_to = participant.participant_email
            sender_email = email_config['sender']
            receiver_email = email_to
            message = MIMEMultipart("alternative")
            message["Subject"] = email_config['subject']
            message["From"] = sender_email
            message["To"] = receiver_email
            exam_code = ''.join(random.choices(string.ascii_letters + string.digits, k=email_config.getint('code_length')))
            part1 = MIMEText(email_config['email_body'] + " " + str(exam_code), "plain")
            message.attach(part1)

            filename = "David_memo_code_eP2Aer.pdf"
            # Open PDF file in binary mode

            # We assume that the file is in the directory where you run your Python script from
            with open(filename, "rb") as attachment:
                # The content type "application/octet-stream" means that a MIME attachment is a binary file
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode to base64
            encoders.encode_base64(part)

            # Add header
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Add attachment to your message and convert it to string
            message.attach(part)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(email_config['host'], email_config.getint('port'), context=context) as server:
                server.login(sender_email, email_config['password'])
                server.sendmail(sender_email, receiver_email, message.as_string())
            paper_instance,paper_instance_stat=Paper_Instance.objects.get_or_create(participant_id=participant.id)
            paper_instance.participant_key = exam_code
            paper_instance.paper_id = participant.paper_id
            paper_instance.save()

    except Exception as e:
        print("Error in sending exam code via email to " + "" + " " + str(e))
        raise

sendEmail()