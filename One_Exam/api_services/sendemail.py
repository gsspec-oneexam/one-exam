# import configparser
# import datetime
# import os
# import smtplib
from calendar import Calendar
from email.mime.base import MIMEBase
from email.utils import formatdate

# import pytz
from django.http import HttpResponse
from django.utils import timezone
# import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys, os, django, datetime, pytz, configparser, ssl, \
    random, string, smtplib, logging
# import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
# import os,datetime
import smtplib

import os,datetime

from api_services.metadata import getConfig, configureLogging

COMMASPACE = ', '

from email import encoders

sys.path.append('D:\projects\pocs\poc')
os.environ['DJANGO_SETTINGS_MODULE'] = 'poc.settings'
django.setup()

from api_services.models import Participant, Paper_Instance, Paper_section, Email_template, Paper, Calender

# config = configparser.ConfigParser()
# config.read(os.environ['OneExamCONFIG'] + '/config.ini')
# config.read('D:\projects\pocs\poc\config.ini')

email_config = getConfig()['SEND_EMAIL_CONFIG']


# CRLF = "\r\n"
# login = "OneExam2020@gmail.com"
# password = "1XAM@6112020"
# attendees = ["srinivasgaddalapalli@gmail.com"]
# organizer = "ORGANIZER;CN=srninvas:mailto:first"+CRLF+" @gmail.com"
# fro = "srinivasgaddalapalli <srinivasgaddalapalli   @gmail.com>"
#
# ddtstart = datetime.datetime.now()
# dtoff = datetime.timedelta(days = 1)
# dur = datetime.timedelta(hours = 1)
# ddtstart = ddtstart +dtoff
# dtend = ddtstart + dur
# dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
# dtstart = ddtstart.strftime("%Y%m%dT%H%M%SZ")
# dtend = dtend.strftime("%Y%m%dT%H%M%SZ")
#
# description = "DESCRIPTION: test invitation from pyICSParser"+CRLF
# attendee = ""
# for att in attendees:
#     attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE"+CRLF+" ;CN="+att+";X-NUM-GUESTS=0:"+CRLF+" mailto:"+att+CRLF
# ical = "BEGIN:VCALENDAR"+CRLF+"PRODID:pyICSParser"+CRLF+"VERSION:2.0"+CRLF+"CALSCALE:GREGORIAN"+CRLF
# ical+="METHOD:REQUEST"+CRLF+"BEGIN:VEVENT"+CRLF+"DTSTART:"+dtstart+CRLF+"DTEND:"+dtend+CRLF+"DTSTAMP:"+dtstamp+CRLF+organizer+CRLF
# ical+= "UID:FIXMEUID"+dtstamp+CRLF
# ical+= attendee+"CREATED:"+dtstamp+CRLF+description+"LAST-MODIFIED:"+dtstamp+CRLF+"LOCATION:"+CRLF+"SEQUENCE:0"+CRLF+"STATUS:CONFIRMED"+CRLF
# ical+= "SUMMARY:test "+ddtstart.strftime("%Y%m%d @ %H:%M")+CRLF+"TRANSP:OPAQUE"+CRLF+"END:VEVENT"+CRLF+"END:VCALENDAR"+CRLF
#
# eml_body = "Email body visible in the invite of outlook and outlook.com but not google calendar"
# eml_body_bin = "This is the email body in binary - two steps"
# msg = MIMEMultipart('mixed')
# msg['Reply-To']=fro
# # msg['Date'] = formatdate(localtime=True)
# msg['Subject'] = "pyICSParser invite"+dtstart
# msg['From'] = fro
# msg['To'] = ",".join(attendees)
#
# part_email = MIMEText(eml_body,"html")
# part_cal = MIMEText(ical,'calendar;method=REQUEST')
#
# msgAlternative = MIMEMultipart('alternative')
# msg.attach(msgAlternative)
#
# ical_atch = MIMEText('application/ics',' ;name="%s"'%("invite.ics"))
# ical_atch.set_payload(ical)
#
#
#
# encoders.encode_base64(ical_atch)
# ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"'%("invite.ics"))
#
# print(ical_atch,'ical')
# eml_atch = MIMEText('', 'plain')
# encoders.encode_base64(eml_atch)
# eml_atch.add_header('Content-Transfer-Encoding', "")
#
# msgAlternative.attach(part_email)
# msgAlternative.attach(part_cal)
#
# mailServer = smtplib.SMTP('smtp.gmail.com', 587)
# mailServer.ehlo()
# mailServer.starttls()
# mailServer.ehlo()
# mailServer.login(login, password)
# mailServer.sendmail(fro, attendees, msg.as_string())
# mailServer.close()
def sendEmail():
    try:

        configureLogging()
        CRLF = "\r\n"
        paper_instances = Paper_Instance.objecs.all()
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
                exam_code = ''.join(
                    random.choices(string.ascii_letters + string.digits, k=email_config.getint('code_length')))
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
                dur = datetime.timedelta(minutes=calender_details.duration)
                examdtend = examdtstart + dur
                dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
                dtstart = examdtstart.strftime("%Y%m%dT%H%M%S")
                dtend = examdtend.strftime("%Y%m%dT%H%M%S")

                description = "DESCRIPTION: exam invitation" + CRLF

                organizer = "ORGANIZER;CN=OneExam:mailto:first" + CRLF + " @gmail.com"
                attendee = "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE" + CRLF + " ;CN=" + receiver_email + " mailto:" + receiver_email + CRLF
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
                logging.info(f"Email sent to mail id:{receiver_email}")

    except Exception as e:
        logging.error(str(e))
        print("Error in sending exam code via email to " + "" + " " + str(e))
        raise


# sendEmail()


def sendEmail_to_participant(participant_id):
    try:

        configureLogging()
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
            exam_code = ''.join(
                random.choices(string.ascii_letters + string.digits, k=email_config.getint('code_length')))
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
            dur = datetime.timedelta(minutes=calender_details.duration)
            examdtend = examdtstart + dur
            dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
            dtstart = examdtstart.strftime("%Y%m%dT%H%M%S")
            dtend = examdtend.strftime("%Y%m%dT%H%M%S")

            description = "DESCRIPTION: exam invitation" + CRLF

            organizer = "ORGANIZER;CN=OneExam:mailto:first" + CRLF + " @gmail.com"
            attendee = "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE" + CRLF + " ;CN=" + receiver_email + " mailto:" + receiver_email + CRLF
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
            logging.info(f"Email sent to mail id:{receiver_email}")

    except Exception as e:
        logging.error(str(e))
        raise
