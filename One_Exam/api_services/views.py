import datetime
import json
from itertools import count
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from api_services.models import Question, Paper_section, Participant, Paper_Instance, Option, Media, Paper, Paper_Question, \
    Paper_answer, Calender
from api_services.sendemail import sendEmail, sendEmail_to_participant

def questionsView(request):
    try:
        response = {
            'data': None,
            'error': None,
            'statusCode': 1
        }
        if request.method == "GET":
            # paper_id = 1
            question_details = Paper_Question.objects.all().order_by('question_order')
            questions_obj = []
            for question_detail in question_details:
                question_db = Question.objects.filter(question_status='A',id=question_detail.question_id)
                for question in question_db:
                    if question.question_type == 'C':
                        options = Option.objects.filter(question_id=question.id).order_by('option_order')
                        temp = {
                            "q_id":question.id,
                            "q_name": question.question,
                            "q_type": question.question_type,
                            "opt1": options[0].option_name,
                            "opt2": options[1].option_name,
                            "opt3": options[2].option_name,
                            "opt4": options[3].option_name,
                            "opt5": options[4].option_name
                        }

                        questions_obj.append(temp)
                    if question.question_type == 'I':
                        temp = {
                                "q_id": question.id,
                                "q_name": question.question,
                                "q_type": question.question_type,
                            }
                        questions_obj.append(temp)
                    if question.question_type == 'P':

                        media = Media.objects.get(id=question.question_image)
                        temp = {
                                "q_id": question.id,
                                "q_name": question.question,
                                "q_type": question.question_type,
                                "mediasource":media.mediasource,
                                "media_url":media.media_url
                            }
                        questions_obj.append(temp)
                    if question.question_type == 'A':

                        media = Media.objects.get(id=question.question_audio)
                        temp = {
                                "q_id": question.id,
                                "q_name": question.question,
                                "q_type": question.question_type,
                                "mediasource":media.mediasource,
                                "media_url":media.media_url
                            }
                        questions_obj.append(temp)
                    if question.question_type == 'R':
                        temp = {
                                "q_id":question.id,
                                "q_name": question.question,
                                "q_type": question.question_type,
                            }
                        questions_obj.append(temp)
            response['data'] = questions_obj
            response['statusCode'] = 0
            return JsonResponse(response)
    except Exception as e:
        print(e)

@csrf_exempt
def oneExamView(request):
    try:
        response = {
            'participant':None,
            'paper_name':None,
            'paper_instance_id':None,
            'Instructions':None,
            'questions':None,
            'section':None,
            'error': None,
            'statusCode': 1
        }
        if request.method == "POST":
            global participant_key, instrctions_obj
            data = json.loads(request.body)
            if data != {}:

                section = []
                participant_key = data['participant_key']
                response['data'] = [{"response": data['participant_key']}]
                participant_details = Paper_Instance.objects.get(participant_key = participant_key)
                paper_id = participant_details.paper_id
                participant_id = participant_details.participant_id
                paper = Paper.objects.get(paper_id = paper_id)
                question_details = Paper_Question.objects.filter(paper_id=paper_id).order_by('question_order')
                questions_obj = []
                for question_detail in question_details:
                    question_db = Question.objects.filter(question_status='A', id=question_detail.question_id)
                    for question in question_db:
                        if question.question_type == 'C':
                            options = Option.objects.filter(question_id=question.id).order_by('option_order')
                            temp = {
                                "q_id":question.id,
                                "q_name": question.question,
                                "q_type": question.question_type,
                                "opt1": options[0].option_name,
                                "opt2": options[1].option_name,
                                "opt3": options[2].option_name,
                                "opt4": options[3].option_name,
                                "opt5": options[4].option_name,
                                "q_time":question_detail.question_time
                            }

                            questions_obj.append(temp)
                        if question.question_type == 'I':
                            temp = {
                                "q_id":question.id,
                                "q_name": question.question,
                                "q_type": question.question_type,
                                "q_time":question_detail.question_time
                            }
                            questions_obj.append(temp)
                        if question.question_type == 'P':
                            media = Media.objects.get(id=question.question_image)
                            temp = {
                                "q_id":question.id,
                                "q_name": question.question,
                                "q_type": question.question_type,
                                "mediasource": media.mediasource,
                                "media_url": media.media_url,
                                "q_time":question_detail.question_time
                            }
                            questions_obj.append(temp)
                        if question.question_type == 'A':
                            media = Media.objects.get(id=question.question_audio)
                            temp = {
                                "q_id":question.id,
                                "q_name": question.question,
                                "q_type": question.question_type,
                                "mediasource": media.mediasource,
                                "media_url": media.media_url,
                                "q_time":question_detail.question_time
                            }
                            questions_obj.append(temp)
                        if question.question_type == 'R':
                            temp = {
                                "q_name": question.question,
                                "q_type": question.question_type,
                                "q_time":question_detail.question_time
                            }
                            questions_obj.append(temp)
                paper_sections = Paper_section.objects.filter(section_paper_id = paper_id)
                for instruction in paper_sections:
                    instrctions_obj = instruction.section_instructions.split("||")
                    section.append(instruction.section_name)
                response['participant'] = participant_id
                response['questions'] = questions_obj
                response['paper_name'] = paper.paper_name
                response['Instructions'] = instrctions_obj
                response['section'] = section
                response['paper_instance_id'] = participant_details.id
                return JsonResponse(response)
            else:
                section = []
                participant_details = Paper_Instance.objects.get(participant_key=participant_key)
                paper_id = participant_details.paper_id
                participant_id = participant_details.participant_id
                q=[]
                paper_answers = Paper_answer.objects.filter(answer_participant_id=participant_id,
                                                            answer_paper_instance_id=participant_details.id)
                answered=[]
                for paper_answer in paper_answers:
                    answered.append(paper_answer.answer_question_id)

                    question_detai = Paper_Question.objects.filter(Q(paper_id=paper_id)).order_by('question_order')

                    q = list(question_detai)

                ques = Paper_Question.objects.filter(Q(paper_id=paper_id),~Q(question_id__in=answered))

                questions_obj = []
                paper_answers = Paper_answer.objects.filter(answer_participant_id= participant_id,
                                                            answer_paper_instance_id=participant_details.id)
                if paper_answers:
                        for question_detail in ques:
                            question_db = Question.objects.filter(question_status='A', id=question_detail.question_id)

                            for question in question_db:

                                        if question.question_type == 'C':
                                            options = Option.objects.filter(question_id=question.id).order_by('option_order')
                                            temp = {
                                                "q_id":question.id,
                                                "q_name": question.question,
                                                "q_type": question.question_type,
                                                "opt1": options[0].option_name,
                                                "opt2": options[1].option_name,
                                                "opt3": options[2].option_name,
                                                "opt4": options[3].option_name,
                                                "opt5": options[4].option_name,
                                                "q_time":question_detail.question_time
                                            }

                                            questions_obj.append(temp)
                                        if question.question_type == 'I':
                                            temp = {
                                                "q_id":question.id,
                                                "q_name": question.question,
                                                "q_type": question.question_type,
                                                "q_time":question_detail.question_time
                                            }
                                            questions_obj.append(temp)
                                        if question.question_type == 'P':
                                            media = Media.objects.get(id=question.question_image)
                                            temp = {
                                                "q_id":question.id,
                                                "q_name": question.question,
                                                "q_type": question.question_type,
                                                "mediasource": media.mediasource,
                                                "media_url": media.media_url,
                                                "q_time":question_detail.question_time
                                            }
                                            questions_obj.append(temp)
                                        if question.question_type == 'A':
                                            media = Media.objects.get(id=question.question_audio)
                                            temp = {
                                                "q_id":question.id,
                                                "q_name": question.question,
                                                "q_type": question.question_type,
                                                "mediasource": media.mediasource,
                                                "media_url": media.media_url,
                                                "q_time":question_detail.question_time
                                            }
                                            questions_obj.append(temp)
                                        if question.question_type == 'R':
                                            temp = {
                                                "q_id":question.id,
                                                "q_name": question.question,
                                                "q_type": question.question_type,
                                                "q_time":question_detail.question_time
                                            }
                                            questions_obj.append(temp)
                else:
                    for question_detail in ques:
                        question_db = Question.objects.filter(question_status='A', id=question_detail.question_id)
                        for question in question_db:
                                if question.question_type == 'C':
                                    options = Option.objects.filter(question_id=question.id).order_by('option_order')
                                    temp = {
                                        "q_id": question.id,
                                        "q_name": question.question,
                                        "q_type": question.question_type,
                                        "opt1": options[0].option_name,
                                        "opt2": options[1].option_name,
                                        "opt3": options[2].option_name,
                                        "opt4": options[3].option_name,
                                        "opt5": options[4].option_name,
                                        "q_time": question_detail.question_time
                                    }

                                    questions_obj.append(temp)
                                if question.question_type == 'I':
                                    temp = {
                                        "q_id": question.id,
                                        "q_name": question.question,
                                        "q_type": question.question_type,
                                        "q_time": question_detail.question_time
                                    }
                                    questions_obj.append(temp)
                                if question.question_type == 'P':
                                    media = Media.objects.get(id=question.question_image)
                                    temp = {
                                        "q_id": question.id,
                                        "q_name": question.question,
                                        "q_type": question.question_type,
                                        "mediasource": media.mediasource,
                                        "media_url": media.media_url,
                                        "q_time": question_detail.question_time
                                    }
                                    questions_obj.append(temp)
                                if question.question_type == 'A':
                                    media = Media.objects.get(id=question.question_audio)
                                    temp = {
                                        "q_id": question.id,
                                        "q_name": question.question,
                                        "q_type": question.question_type,
                                        "mediasource": media.mediasource,
                                        "media_url": media.media_url,
                                        "q_time": question_detail.question_time
                                    }
                                    questions_obj.append(temp)
                                if question.question_type == 'R':
                                    temp = {
                                        "q_id": question.id,
                                        "q_name": question.question,
                                        "q_type": question.question_type,
                                        "q_time": question_detail.question_time
                                    }
                                    questions_obj.append(temp)
                response['questions'] = questions_obj
                participant_id = participant_details.participant_id
                paper = Paper.objects.get(paper_id=paper_id)
                paper_sections = Paper_section.objects.filter(section_paper_id = paper_id)
                for instruction in paper_sections:
                    instrctions_obj = instruction.section_instructions.split("||")
                    section.append(instruction.section_name)
                response['participant'] = participant_id
                response['paper_name'] = paper.paper_name
                response['paper_instance_id'] = participant_details.id
                response['Instructions'] = instrctions_obj
                response['section'] = section
                participant_key = ""
                return JsonResponse(response)
        if request.method == "GET":
            instrc_db = Paper_section.objects.all()
            instrctions_obj = []
            for instruction in instrc_db:
                temp = {
                    "sect_paper_id": instruction.section_paper_id,
                    "sect_name": instruction.section_name,
                    "sect_ins": instruction.section_instructions,
                    "sect_marks": instruction.section_marks,
                }
                instrctions_obj.append(temp)
            response['data'] = instrctions_obj
            response['statusCode'] = 0
            return JsonResponse(response)
    except Exception as e:
        print(e)


@csrf_exempt
def exam_answers(request):
    try:
        response = {
            'data':None,
            'error': None,
            'statusCode': 1
        }
        if request.method == "POST":
            data = json.loads(request.body)
            paper_details = Paper.objects.get(paper_name=data['paper_name'])
            paper_answer, paper_answer_stat = Paper_answer.objects.get_or_create(
                                                        answer_paper_instance_id=data['paper_instance_id'],
                                                        answer_paper_id=paper_details.paper_id,
                                                        answer_participant_id=data['participant_id'],
                                                        answer_question_id=data['question_id']
                                                        )
            paper_answer.answer_subject_id = paper_details.paper_subject
            if 'ans' in data:
                paper_answer.answer_question_response = data['ans']
                paper_answer.answer_date = datetime.datetime.now()
            else:
                paper_answer.answer_question_response = "null"
                paper_answer.answer_date = datetime.datetime.now()
            paper_answer.save()
            return JsonResponse(response)
    except Exception as e:
        print(e)

def exam_code_verification_view(request):
    try:
        response = {
            'data': None,
            'error': None,
            'statusCode': 1
        }
        if request.method == "GET":
            exam_codes = Paper_Instance.objects.filter(participant_key__isnull=False)
            exam_code_obj = []
            for exam_code in exam_codes:
                calender_details = Calender.objects.get(id=exam_code.calender_id)
                if ((calender_details.schedule_time - datetime.timedelta(
                        minutes=6)) <= datetime.datetime.now() <= calender_details.schedule_time) or \
                        (calender_details.schedule_time < datetime.datetime.now() < (
                                calender_details.schedule_time + datetime.timedelta(
                            minutes=calender_details.duration))):
                    exam_code_obj.append(exam_code.participant_key)
            response['data'] = exam_code_obj
            response['statusCode'] = 0
            return JsonResponse(response)
    except Exception as e:
        print(e)


@csrf_exempt
def examinar_dashboard(request):
    response = {
        'participants': None,
        'total_papers': None,
        'papers':None,
        'error': None,
        'statusCode': 1
    }
    try:
        papers = Paper.objects.all()
        students = Participant.objects.all()
        papers_obj =[]
        for paper in papers:
            temp={
                'paper_id':paper.id,
                'paper_name':paper.paper_name,
            }
            papers_obj.append(temp)
        response['total_papers'] = len(papers)
        response['papers'] = papers_obj
        response['participants'] = len(students)
        response['statusCode'] = 0
        return JsonResponse(response)

    except Exception as e:
        print(e)


@csrf_exempt
def participant_form(request):
    try:
        response = {
            'data':None,
            'error': None,
            'statusCode': 1
        }
        if request.method == "POST":
            data = json.loads(request.body)
            Participant(first_name = data['first_name'],
                        last_name = data['last_name'],
                        registration_date = datetime.datetime.now(),
                        company_id = 1,
                        paper_id = data['paper_id'],
                        participant_email = data['email'],
                        participant_phone = data['mobile_no'],
                        participant_city = data['City'],
                        participant_state = data['state'],
                        participant_country=data['country']).save()
            response['statusCode'] = 2
            calender = Calender.objects.get(paper_id=data['paper_id'])
            Paper_Instance(paper_id=data['paper_id'],participant_id=Participant.objects.latest('id').id,
                           calender_id=calender.id).save()
            sendEmail_to_participant(Participant.objects.latest('id').id)
            return JsonResponse(response)
    except Exception as e:
        print(e)