# import json
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
# from backend.models import Question, Paper_section, Participant, Paper_Instance, Option, Media, Paper
#
#
# def questions(paper_id):
#     try:
#         question_db = Question.objects.filter(question_status='A')
#         questions_obj = []
#         for question in question_db:
#
#             if question.question_type == 'C':
#                 options = Option.objects.filter(question_id=question.id)
#                 temp = {
#                     "q_name": question.question,
#                     "q_type": question.question_type,
#                     "opt1": options[0].option_name,
#                     "opt2": options[1].option_name,
#                     "opt3": options[2].option_name,
#                     "opt4": options[3].option_name,
#                     "opt5": options[4].option_name
#                 }
#
#                 questions_obj.append(temp)
#             if question.question_type == 'I':
#                 temp = {
#                     "q_name": question.question,
#                     "q_type": question.question_type,
#                 }
#                 questions_obj.append(temp)
#             if question.question_type == 'P':
#                 media = Media.objects.get(id=question.question_image)
#                 temp = {
#                     "q_name": question.question,
#                     "q_type": question.question_type,
#                     "mediaorigin": media.mediaorigin,
#                     "media_url": media.media_url
#                 }
#                 questions_obj.append(temp)
#             if question.question_type == 'A':
#                 media = Media.objects.get(id=question.question_audio)
#                 temp = {
#                     "q_name": question.question,
#                     "q_type": question.question_type,
#                     "mediaorigin": media.mediaorigin,
#                     "media_url": media.media_url
#                 }
#                 questions_obj.append(temp)
#             if question.question_type == 'R':
#                 temp = {
#                     "q_name": question.question,
#                     "q_type": question.question_type,
#                 }
#                 questions_obj.append(temp)
#         return questions_obj
#     except Exception as e:
#         print(e)
