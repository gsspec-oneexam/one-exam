import configparser
import datetime
import os
import smtplib
from django.utils import timezone
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random, string

import sys, os, django
sys.path.append('S:/3.12.2020/one-exam/One_Exam')
os.environ['DJANGO_SETTINGS_MODULE'] = 'poc.settings'
django.setup()

from backend.models import Participant, Paper_Instance, Paper_section, Email_template, Paper, Calender

config = configparser.ConfigParser()
# config.read(os.environ['OneExamCONFIG'] + '/config.ini')

config.read('D:\projects\pocs\poc\config.ini')
email_config = config['SEND_EMAIL_CONFIG']
paper_instances = Paper_Instance.objects.all()

for paper_instance in paper_instances:
    participant = Participant.objects.get(id=paper_instance.participant_id)
    # paper = Paper.objects.get(paper_id=participant.paper_id)
    calender_details = Calender.objects.get(id = paper_instance.calender_id)
    import dateutil.parser

    print(dateutil.parser.parse(str(calender_details.schedule_time)),"parseing")
    print(calender_details.schedule_time-datetime.timedelta(minutes=10),"\n",datetime.datetime.now())
    if datetime.datetime.now() <= calender_details.schedule_time-datetime.timedelta(minutes=10):
        print("expired")
    # print(calender_details.schedule_time.strftime("%A %d %B %Y, %I:%M %p " ))
    # print(timezone.localtime(calender_details.schedule_time).strftime("%A %d %B %Y, %I:%M %p %Z"))

# name = "Dan"
# age = 21
#you need to have that "f" before the string
# name_and_age = "My name is {name}, and I am {age} \n years old."
# email_template = Email_template.objects.get(company_id=1)
# name = "Srinivas"
# print(email_template.email_body.replace("{name}",name).replace("{n}","\n").replace("{paper}","carnatic"))
def sendEmail():
    try:
        paper_instances = Paper_Instance.objects.all()
        for paper_instance in paper_instances:
            participant = Participant.objects.get(id=paper_instance.participant_id)
            email_template = Email_template.objects.get(company_id=participant.company_id)
            email_to = participant.participant_email
            sender_email = email_config['sender']
            receiver_email = email_to
            message = MIMEMultipart("alternative")
            message["Subject"] = email_template.email_subject
            message["From"] = sender_email
            message["To"] = receiver_email
            exam_code = ''.join(random.choices(string.ascii_letters + string.digits, k=email_config.getint('code_length')))
            paper = Paper.objects.get(paper_id=participant.paper_id)
            calender_details = Calender.objects.get(id=paper_instance.calender_id)
            emailbody = MIMEText(email_template.email_body
                                 .replace("{name}",participant.first_name)
                                 .replace("{paper}",paper.paper_name)
                                 .replace("{date}", calender_details.schedule_time.strftime("%A %d %B %Y"))
                                 .replace("{time}", calender_details.schedule_time.strftime(" %I:%M %p " ))
                                 .replace("{link}", email_config['url'])
                                 .replace("{code}", str(exam_code))
                                 .replace("{n}","\n"))
            message.attach(emailbody)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(email_config['host'], email_config.getint('port'), context=context) as server:
                server.login(sender_email, email_config['password'])
                server.sendmail(sender_email, receiver_email, message.as_string())
            # paper_instance,paper_instance_stat=Paper_Instance.objects.get_or_create(participant_id=participant.id)
            paper_instance.participant_key = exam_code
            paper_instance.paper_instance_date = datetime.datetime.now()
            paper_instance.save()

    except Exception as e:
        print("Error in sending exam code via email to " + "" + " " + str(e))
        raise

# sendEmail()


