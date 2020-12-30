import configparser
import datetime
import os
import smtplib
from calendar import Calendar
from email.mime.base import MIMEBase
from email.utils import formatdate

import pytz
from django.http import HttpResponse
from django.utils import timezone
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random, string
import sys, os, django
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
import os,datetime
COMMASPACE = ', '

from email import encoders

sys.path.append('D:\projects\pocs\poc')
os.environ['DJANGO_SETTINGS_MODULE'] = 'poc.settings'
django.setup()

from backend.models import Participant, Paper_Instance, Paper_section, Email_template, Paper, Calender

config = configparser.ConfigParser()
# config.read(os.environ['OneExamCONFIG'] + '/config.ini')
config.read('D:\projects\pocs\poc\config.ini')
import smtplib

import os,datetime
email_config=config['SEND_EMAIL_CONFIG']

def sendEmail():
    try:
        CRLF = "\r\n"
        paper_instances = Paper_Instance.objects.all()
        for paper_instance in paper_instances:
            calender_details = Calender.objects.get(id=paper_instance.calender_id)
            if calender_details.schedule_time > datetime.datetime.now():
                participant = Participant.objects.get(id=paper_instance.participant_id)
                email_template = Email_template.objects.get(company_id=participant.company_id)
                sender_email = email_config['sender']
                receiver_email = participant.participant_email
                message = MIMEMultipart("mixed")
                message["Subject"] = email_template.email_subject
                message["From"] = f"OneExam <{sender_email}>"
                message["To"] = receiver_email
                exam_code = ''.join(random.choices(string.ascii_letters + string.digits, k=email_config.getint('code_length')))
                paper = Paper.objects.get(paper_id=participant.paper_id)

                emailbody = MIMEText(email_template.email_body
                                     .replace("{name}", participant.first_name)
                                     .replace("{paper}", paper.paper_name)
                                     .replace("{date}", calender_details.schedule_time.strftime("%A %d %B %Y"))
                                     .replace("{time}", calender_details.schedule_time.strftime(" %I:%M %p "))
                                     .replace("{link}", email_config['url'])
                                     .replace("{code}", str(exam_code))
                                     .replace("{n}", "\n"))
                message.attach(emailbody)


                examdtstart = calender_details.schedule_time
                dur = datetime.timedelta(minutes = calender_details.duration )
                examdtend =  examdtstart + dur
                dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
                dtstart = examdtstart.strftime("%Y%m%dT%H%M%S")
                dtend = examdtend.strftime("%Y%m%dT%H%M%S")

                description = "DESCRIPTION: exam invitation" + CRLF

                organizer = "ORGANIZER;CN=OneExam:mailto:first" + CRLF + " @gmail.com"
                attendee = "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE" + CRLF + " ;CN=" + receiver_email +  " mailto:" + receiver_email + CRLF
                ical = "BEGIN:VCALENDAR" + CRLF + "PRODID:pyICSParser" + CRLF + "VERSION:2.0" + CRLF + "CALSCALE:GREGORIAN" + CRLF
                ical += "METHOD:REQUEST" + CRLF + "BEGIN:VEVENT" + CRLF + "DTSTART:" + dtstart + CRLF + "DTEND:" + dtend + CRLF + "DTSTAMP:" + dtstamp + CRLF + organizer + CRLF
                ical += "UID:FIXMEUID" + dtstamp + CRLF
                ical += attendee + "CREATED:" + dtstamp + CRLF + description + "LAST-MODIFIED:" + dtstamp + CRLF + "LOCATION:" + CRLF + "SEQUENCE:0" + CRLF + "STATUS:CONFIRMED" + CRLF
                ical += "SUMMARY:Exam invitation " + CRLF + "TRANSP:OPAQUE" + CRLF + "END:VEVENT" + CRLF + "END:VCALENDAR" + CRLF

                eml_body = "\n.ics file will be visible in the invite of outlook and outlook.com but not google calendar"
                eml_body_bin = "This is the email body in binary - two steps"
                # message = MIMEMultipart('mixed')

                part_email = MIMEText(eml_body)
                message.attach(part_email)
                part_cal = MIMEText(ical, 'calendar;method=REQUEST')

                msgAlternative = MIMEMultipart('alternative')
                message.attach(msgAlternative)

                ical_atch = MIMEText('application/ics', ' ;name="%s"' % ("Exam invitation.ics"))
                ical_atch.set_payload(ical)

                encoders.encode_base64(ical_atch)
                ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"' % ("invite.ics"))

                eml_atch = MIMEText('', 'plain')
                encoders.encode_base64(eml_atch)
                eml_atch.add_header('Content-Transfer-Encoding', "")

                # msgAlternative.attach(part_email)
                msgAlternative.attach(part_cal)

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(email_config['host'], email_config.getint('port'), context=context) as server:
                    server.login(sender_email, email_config['password'])
                    server.sendmail(sender_email, receiver_email, message.as_string())
                # paper_instance,paper_instance_stat=Paper_Instance.objects.get_or_create(participant_id=participant.id)
                paper_instance.participant_key = exam_code
                paper_instance.paper_instance_date = datetime.datetime.now()
                paper_instance.save()
                print(f"Email sent to mail id:{receiver_email}")

    except Exception as e:
        print("Error in sending exam code via email to " + "" + " " + str(e))
        raise

# sendEmail()



def sendEmail_to_participant(participant_id):
    try:
        CRLF = "\r\n"
        paper_instance = Paper_Instance.objects.get(participant_id=participant_id)
        # for paper_instance in paper_instances:
        calender_details = Calender.objects.get(id=paper_instance.calender_id)
        if calender_details.schedule_time > datetime.datetime.now():
            participant = Participant.objects.get(id=paper_instance.participant_id)
            email_template = Email_template.objects.get(company_id=participant.company_id)
            sender_email = email_config['sender']
            receiver_email = participant.participant_email
            message = MIMEMultipart("mixed")
            message["Subject"] = email_template.email_subject
            message["From"] = f"OneExam <{sender_email}>"
            message["To"] = receiver_email
            exam_code = ''.join(random.choices(string.ascii_letters + string.digits, k=email_config.getint('code_length')))
            paper = Paper.objects.get(paper_id=participant.paper_id)
            emailbody = MIMEText(email_template.email_body
                                 .replace("{name}", participant.first_name)
                                 .replace("{paper}", paper.paper_name)
                                 .replace("{date}", calender_details.schedule_time.strftime("%A %d %B %Y"))
                                 .replace("{time}", calender_details.schedule_time.strftime(" %I:%M %p "))
                                 .replace("{link}", email_config['url'])
                                 .replace("{code}", str(exam_code))
                                 .replace("{n}", "\n"))
            message.attach(emailbody)


            examdtstart = calender_details.schedule_time
            dur = datetime.timedelta(minutes = calender_details.duration )
            examdtend =  examdtstart + dur
            dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
            dtstart = examdtstart.strftime("%Y%m%dT%H%M%S")
            dtend = examdtend.strftime("%Y%m%dT%H%M%S")

            description = "DESCRIPTION: exam invitation" + CRLF

            organizer = "ORGANIZER;CN=OneExam:mailto:first" + CRLF + " @gmail.com"
            attendee = "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE" + CRLF + " ;CN=" + receiver_email +  " mailto:" + receiver_email + CRLF
            ical = "BEGIN:VCALENDAR" + CRLF + "PRODID:pyICSParser" + CRLF + "VERSION:2.0" + CRLF + "CALSCALE:GREGORIAN" + CRLF
            ical += "METHOD:REQUEST" + CRLF + "BEGIN:VEVENT" + CRLF + "DTSTART:" + dtstart + CRLF + "DTEND:" + dtend + CRLF + "DTSTAMP:" + dtstamp + CRLF + organizer + CRLF
            ical += "UID:FIXMEUID" + dtstamp + CRLF
            ical += attendee + "CREATED:" + dtstamp + CRLF + description + "LAST-MODIFIED:" + dtstamp + CRLF + "LOCATION:" + CRLF + "SEQUENCE:0" + CRLF + "STATUS:CONFIRMED" + CRLF
            ical += "SUMMARY:Exam invitation " + CRLF + "TRANSP:OPAQUE" + CRLF + "END:VEVENT" + CRLF + "END:VCALENDAR" + CRLF

            eml_body = "\n.ics file will be visible in the invite of outlook and outlook.com but not google calendar"
            eml_body_bin = "This is the email body in binary - two steps"
            # message = MIMEMultipart('mixed')

            part_email = MIMEText(eml_body)
            message.attach(part_email)
            part_cal = MIMEText(ical, 'calendar;method=REQUEST')

            msgAlternative = MIMEMultipart('alternative')
            message.attach(msgAlternative)

            ical_atch = MIMEText('application/ics', ' ;name="%s"' % ("Exam invitation.ics"))
            ical_atch.set_payload(ical)

            encoders.encode_base64(ical_atch)
            ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"' % ("invite.ics"))

            eml_atch = MIMEText('', 'plain')
            encoders.encode_base64(eml_atch)
            eml_atch.add_header('Content-Transfer-Encoding', "")

            # msgAlternative.attach(part_email)
            msgAlternative.attach(part_cal)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(email_config['host'], email_config.getint('port'), context=context) as server:
                server.login(sender_email, email_config['password'])
                server.sendmail(sender_email, receiver_email, message.as_string())
            # paper_instance,paper_instance_stat=Paper_Instance.objects.get_or_create(participant_id=participant.id)
            paper_instance.participant_key = exam_code
            paper_instance.paper_instance_date = datetime.datetime.now()
            paper_instance.save()
            print(f"Email sent to mail id:{receiver_email}")

    except Exception as e:
        print("Error in sending exam code via email to " + "" + " " + str(e))
        raise

