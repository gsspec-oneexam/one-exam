from django.db import models

"""
Created by : Srinivas.
Created on : 31 OCT 2020.
desc: To store question details.
"""
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=256)
    question_type = models.CharField(max_length=20)

    question_audio = models.IntegerField(null=True,blank=True)

    question_video = models.IntegerField(null=True,blank=True)

    question_complexity = models.IntegerField(null=True,blank=True)

    question_marks = models.IntegerField(null=True,blank=True)

    question_topic = models.IntegerField(null=True,blank=True)

    question_subtopic = models.IntegerField(null=True,blank=True)

    question_tags = models.CharField(max_length=256,null=True,blank=True)


    question_status = models.CharField(max_length=256,null=True,blank=True)
    q_choices = models.CharField(max_length=125)

    class Meta:
        db_table = 'question'



class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=125, null=True)
    q_type = models.CharField(max_length=20)
    answer = models.CharField(max_length=100, null=True)

   


"""
Created by : Srinivas.
Created on : 31 OCT 2020.
desc: To store Section details.
"""
class Paper_section(models.Model):
    id = models.AutoField(primary_key=True)
    section_paper_id = models.IntegerField(null=True)
    section_name = models.CharField(max_length=20)
    section_instructions = models.CharField(max_length=400, null=True)
    section_marks = models.CharField(max_length=400, null=True)

    class Meta:
        db_table = 'paper_section'


class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    participant_email = models.CharField(max_length=100,null=True)
    participant_phone = models.CharField(max_length=40,null=True)

    class Meta:
        db_table = 'participant'


class Paper_Instance(models.Model):
    id = models.AutoField(primary_key=True)
    paper_id = models.CharField(max_length=100,null=True)
    participant_id = models.CharField(max_length=100,null=True)
    participant_key = models.CharField(max_length=100,null=True)
    calender_id = models.CharField(max_length=40,null=True)

    class Meta:
        db_table = 'paper_instance'