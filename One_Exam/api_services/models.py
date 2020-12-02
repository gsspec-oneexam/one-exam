from django.db import models


"""
Created by : Srinivas.
Created on : 12 November 2020.
desc: To store Organization details.
"""
class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=100)
    class Meta:
        db_table = 'organization'

"""
Created by : Srinivas.
Created on : 12 November 2020.
desc: To store domain details.
"""
class Domain(models.Model):
    id = models.AutoField(primary_key=True)
    domain_code = models.CharField(max_length=3)
    domain_name = models.CharField(max_length=100)
    domain_status = models.CharField(max_length=1)
    class Meta:
        db_table = 'domain'


"""
Created by : Srinivas.
Created on : 12 November 2020.
desc: To store company details.
"""
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_add1 = models.CharField(max_length=100,null=True,blank=True)
    company_add2 = models.CharField(max_length=100,null=True,blank=True)
    company_city = models.CharField(max_length=100,null=True,blank=True)
    company_state = models.CharField(max_length=100,null=True,blank=True)
    company_country = models.CharField(max_length=100,null=True,blank=True)
    company_domain = models.CharField(max_length=4,null=True,blank=True)
    company_status = models.CharField(max_length=1,null=True,blank=True)
    company_organization = models.IntegerField()
    company_website = models.CharField(max_length=100,null=True,blank=True)
    company_phone1 = models.CharField(max_length=100,null=True,blank=True)
    company_phone2 = models.CharField(max_length=100,null=True,blank=True)
    company_email = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        db_table = 'company'


"""
Created by : Srinivas.
Created on : 12 November 2020.
desc: To store user details.
"""
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=1,null=True,blank=True)
    dateofcreation = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    dateofupdation = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    class Meta:
        db_table = 'user'


"""
Created by : Srinivas.
Created on : 31 OCT 2020.
desc: To store Exam schedule details.
"""
class Calender(models.Model):
    id = models.AutoField(primary_key=True)
    paper_id = models.IntegerField()
    participant_instance_id = models.IntegerField()
    schedule_time = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()

    class Meta:
        db_table = 'calender'


"""
Created by : Srinivas.
Created on : 31 OCT 2020.
desc: To store Paper_Instance details.
"""
class Paper_Instance(models.Model):
    id = models.AutoField(primary_key=True)
    paper_id = models.IntegerField(null=True,blank=True)
    participant_id = models.IntegerField()
    calender_id = models.IntegerField(null=True,blank=True)
    participant_key = models.CharField(max_length=16)
    paper_instance_date = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = 'paper_instance'

"""
Created by : Srinivas.
Created on : 12 November 2020.
desc: To store Topic details.
"""
class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    topic_name = models.CharField(max_length=100)
    topic_status = models.CharField(max_length=1)
    class Meta:
        db_table = 'topic'

"""
Created by : Srinivas.
Created on : 12 November 2020.
desc: To store Topic details.
"""
class Sub_topic(models.Model):
    id = models.AutoField(primary_key=True)
    subtopic_name = models.CharField(max_length=100)
    subtopic_status = models.CharField(max_length=1)
    subtopic_topic = models.IntegerField()
    class Meta:
        db_table = 'subtopic'

"""
Created by : Srinivas.
Created on : 12 November 2020.
desc: To store subject details.
"""
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100,null=True,blank=True)
    subject_status = models.CharField(max_length=1,null=True,blank=True)
    class Meta:
        db_table = 'subject'

"""
Created by : Srinivas.
Created on : 31 OCT 2020.
desc: To store Option details.
"""
class Paper(models.Model):
    id = models.AutoField(primary_key=True)
    paper_id = models.IntegerField(null=True,blank=True)
    paper_name = models.CharField(max_length=100,null=True)
    paper_marks = models.IntegerField()
    paper_instructions = models.CharField(max_length=256,null=True)
    paper_subject = models.IntegerField()
    paper_level = models.CharField(max_length=40)

    class Meta:
        db_table = 'paper'



"""
Created by : Srinivas.
Created on : 11 October 2020.
desc: To store Paper question details.
"""
class Paper_Question(models.Model):
    id = models.AutoField(primary_key=True)
    paper_id = models.IntegerField(null=True,blank=True)
    question_id = models.IntegerField(null=True,blank=True)
    section_id = models.IntegerField(null=True,blank=True)
    question_order = models.IntegerField(null=True,blank=True)
    question_type = models.CharField(max_length=1,null=True,blank=True)
    question_level = models.IntegerField(null=True,blank=True)
    question_marks = models.IntegerField(null=True,blank=True)
    question_topic = models.IntegerField(null=True,blank=True)
    question_subtopic = models.IntegerField(null=True,blank=True)
    question_time = models.IntegerField(null=True,blank=True)
    class Meta:
        db_table = 'paper_question'


"""
Created by : Srinivas.
Created on : 31 OCT 2020.
desc: To store question details.
"""
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=256)
    question_type = models.CharField(max_length=1)
    question_audio = models.IntegerField(null=True,blank=True)
    question_image = models.IntegerField(null=True,blank=True)
    question_video = models.IntegerField(null=True,blank=True)
    question_complexity = models.IntegerField(null=True,blank=True)
    question_marks = models.IntegerField(null=True,blank=True)
    question_topic = models.IntegerField(null=True,blank=True)
    question_subtopic = models.IntegerField(null=True,blank=True)
    question_tags = models.CharField(max_length=256,null=True,blank=True)
    question_status = models.CharField(max_length=1,null=True,blank=True)
    createdby = models.IntegerField(null=True,blank=True)
    updatedby = models.IntegerField(null=True,blank=True)
    question_lastused = models.DateTimeField(null=True)
    dateofcreation = models.DateTimeField(null=True,blank=True)
    dateofupdation = models.DateTimeField(null=True,blank=True)
    question_group = models.CharField(max_length=3,null=True,blank=True)

    class Meta:
        db_table = 'question'


"""
Created by : Srinivas.
Created on : 31 OCT 2020.
desc: To store Option details.
"""
class Option(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.IntegerField(null=True,blank=True)
    option_name = models.CharField(max_length=100,null=True)
    option_order = models.IntegerField(null=True,blank=True)
    option_answer = models.CharField(max_length=1,null=True)

    class Meta:
        db_table = 'option'

"""
Created by : Srinivas.
Created on : 12 November 2020.
desc: To store Paper answers details.
"""
class Paper_answer(models.Model):
    id = models.AutoField(primary_key=True)
    answer_date = models.DateTimeField(null=True)
    answer_paper_id = models.IntegerField()
    answer_paper_instance_id = models.IntegerField()
    answer_subject_id = models.IntegerField(null=True,blank=True)
    answer_question_id = models.IntegerField()
    answer_participant_id = models.IntegerField()
    answer_question_response = models.CharField(max_length=256,null=True,blank=True)
    answer_correct = models.CharField(max_length=1,null=True,blank=True)
    aswer_time_given = models.IntegerField(null=True,blank=True)
    asnwer_time_used = models.IntegerField(null=True,blank=True)
    class Meta:
        db_table = 'paper_answer'

"""
Created by : Srinivas.
Created on : 12 November 2020.
desc: To store Media details.
"""
class Media(models.Model):
    id = models.AutoField(primary_key=True)
    media_type = models.CharField(max_length=1)
    mediasource = models.CharField(max_length=1,null=True,blank=True)
    mediaorigin = models.CharField(max_length=1,null=True,blank=True)
    media_url = models.CharField(max_length=256,null=True,blank=True)
    createdby = models.IntegerField(null=True,blank=True)
    updatedby = models.IntegerField(null=True,blank=True)
    dateofcreation = models.DateTimeField(null=True,blank=True)
    dateofupdation = models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'media'


   


"""
Created by : Srinivas.
Created on : 31 OCT 2020.
desc: To store Paper_Section details.
"""
class Paper_section(models.Model):
    id = models.AutoField(primary_key=True)
    section_paper_id = models.IntegerField(null=True)
    section_name = models.CharField(max_length=100,null=True)
    section_instructions = models.CharField(max_length=400, null=True)
    section_marks = models.IntegerField(null=True)

    class Meta:
        db_table = 'paper_section'


"""
Created by : Srinivas.
Created on : 31 OCT 2020.
desc: To store Participant details.
"""
class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    registration_date = models.DateTimeField(null=True)
    company_id = models.IntegerField(null=True,blank=True)
    paper_id = models.IntegerField(null=True,blank=True)
    participant_email = models.CharField(max_length=100,null=True)
    participant_phone = models.CharField(max_length=40,null=True)
    participate_add1 = models.CharField(max_length=100,null=True)
    participate_add2 = models.CharField(max_length=100,null=True)
    participant_city = models.CharField(max_length=100,null=True)
    participant_state = models.CharField(max_length=100,null=True)
    participant_country = models.CharField(max_length=40,null=True)
    class Meta:
        db_table = 'participant'



"""
Created by : Srinivas.
Created on : 31 OCT 2020.
desc: To store Paper_results details.
"""
class Paper_results(models.Model):
    id = models.AutoField(primary_key=True)
    paper_id = models.IntegerField()
    participant_id = models.IntegerField()
    calender_id = models.IntegerField()
    participant_key = models.CharField(max_length=16)
    paper_instance_date = models.DateTimeField()
    paper_participate_result = models.CharField(max_length=1,null=True,blank=True)
    paper_participate_grade = models.CharField(max_length=10,null=True,blank=True)
    paper_result_status = models.CharField(max_length=1,null=True,blank=True)

    class Meta:
        db_table = 'paper_results'

class Poc_marks_memo(models.Model):
    id = models.AutoField(primary_key=True)
    std_name = models.CharField(max_length=100,null=True,blank=True)
    father_name = models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=300,null=True,blank=True)
    place = models.CharField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    grade = models.CharField(max_length=1,null=True,blank=True)
    paper1 = models.CharField(max_length=100,null=True,blank=True)
    paper2 = models.CharField(max_length=100,null=True,blank=True)
    paper1_marks_required = models.IntegerField(null=True,blank=True)
    paper2_marks_required = models.IntegerField(null=True,blank=True)
    paper1_marks_obtained = models.IntegerField(null=True,blank=True)
    paper2_marks_obtained = models.IntegerField(null=True,blank=True)

    class Meta:
        db_table = 'poc_marks_memo'