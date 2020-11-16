import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from api_services.models import Question, Paper_section, Participant, Paper_Instance


def questionsView(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    if request.method == "GET":
        question_db = Question.objects.all()
        questions_obj=[]
        for question in question_db:
            temp={
                "q_name":question.question,
                "q_type":question.question_type,
                "opt1":question.q_choices.split(",")[0],
                "opt2":question.q_choices.split(",")[1],
                "opt3": question.q_choices.split(",")[2],
                "opt4": question.q_choices.split(",")[3],
                "opt5": question.q_choices.split(",")[4],
            }
            questions_obj.append(temp)
        response['data'] = questions_obj
        response['statusCode'] = 0
        return JsonResponse(response)


def instructionsView(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    if request.method == "GET":
        instrc_db = Paper_section.objects.all()
        instrctions_obj=[]
        for instruction in instrc_db:
            temp={
                "sect_paper_id":instruction.section_paper_id,
                "sect_name":instruction.section_name,
                "sect_ins":instruction.section_instructions,
                "sect_marks":instruction.section_marks,
                }
            instrctions_obj.append(temp)
        response['data'] = instrctions_obj
        response['statusCode'] = 0
        return JsonResponse(response)


def exam_code_verification_view(request):
    response = {
        'data': None,
        'error': None,
        'statusCode': 1
    }
    if request.method == "GET":
        exam_codes = Paper_Instance.objects.all()
        exam_code_obj = []
        for exam_code in exam_codes:
            temp = {
                "exam_code": exam_code.participant_key,
            }
            exam_code_obj.append(temp)
        response['data'] = exam_code_obj
        response['statusCode'] = 0
        return JsonResponse(response)