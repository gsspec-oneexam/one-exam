from django.contrib import admin
from django.urls import path, include
from api_services import views

urlpatterns = [
    path('questions', views.questionsView),
    path('oneexam', views.oneExamView),
    path('exam_ans', views.exam_answers),
    path('exam_codes',views.exam_code_verification_view),
    path('dashboard', views.examinar_dashboard),

]