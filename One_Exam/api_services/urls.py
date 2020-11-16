from django.contrib import admin
from django.urls import path, include
from api_services import views

urlpatterns = [
    path('questions', views.questionsView),
    path('sec_instructions', views.instructionsView),
    path('exam_codes',views.exam_code_verification_view)

]