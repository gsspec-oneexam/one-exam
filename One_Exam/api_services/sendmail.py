import configparser
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random, string

import sys, os, django
sys.path.append('S:\GS_spec\One_Exam')
os.environ['DJANGO_SETTINGS_MODULE'] = 'One_Exam.settings'
django.setup()

from api_services.models import Participant, Paper_Instance

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
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(email_config['host'], email_config.getint('port'), context=context) as server:
                server.login(sender_email, email_config['password'])
                server.sendmail(sender_email, receiver_email, message.as_string())
            paper_instance,paper_instance_stat=Paper_Instance.objects.get_or_create(participant_id=participant.id)
            paper_instance.participant_key = exam_code
            paper_instance.save()

    except Exception as e:
        print("Error in sending exam code via email to " + "" + " " + str(e))
        raise

sendEmail()