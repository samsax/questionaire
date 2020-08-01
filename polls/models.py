from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django import forms
from django.utils.timezone import now

class Questionnaire(models.Model):
    questionnaire_title = models.CharField(max_length=300)
    questionnaire_description = models.CharField(max_length=500)
    def __str__(self):
        return self.questionnaire_title


class Journey(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, 
        on_delete=models.DO_NOTHING, 
        blank=True,
        null=True )
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    status = models.IntegerField('Status, 1 active 0 desactive')


class Question(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    question_type = models.IntegerField('Type question, 1 open question, 2 Chosee one, 3 Multiple chosee', default=1)
    questionnaire = models.ForeignKey(Questionnaire, 
        on_delete=models.DO_NOTHING, 
        blank=True,
        null=True )
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500,default='')
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE,
        blank=True,
        null=True )
    def __str__(self):
        return '{} ({})'.format(self.question.question_text, self.choice_text)

class ResponseCovid(models.Model):
    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=None)
    # date_response = models.DateField(default=now)
    question = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=500,default='')
    choice_value = models.IntegerField(default=0)
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE,
        blank=True,
        null=True)
    def __str__(self):
        return '{} ({}) {}'.format(self.question, self.choice_text, self.choice_value)

class Part(models.Model):
    part_title = models.CharField(max_length=300)
    part_description = models.CharField(max_length=500,
        blank=True,
        null=True)
    def __str__(self):
        return self.part_title

class QuestionnairePart(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, 
        on_delete=models.DO_NOTHING, 
        blank=True,
        null=True )
    part =  models.ForeignKey(Part, 
        on_delete=models.DO_NOTHING, 
        blank=True,
        null=True )
    order_questionnaire = models.IntegerField(default=1)
    def __str__(self):
        return self.questionnaire.questionnaire_title +' '+ self.part.part_title
    



class PartQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    part =  models.ForeignKey(Part, 
        on_delete=models.DO_NOTHING, 
        blank=True,
        null=True )
    order_question = models.IntegerField(default=1)
    def __str__(self):
        return self.question.question_text


class ResponseQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice =  models.ForeignKey(Choice, 
        on_delete=models.DO_NOTHING, 
        blank=True,
        null=True )
    def __str__(self):
        return "%s %s" % (self.question.question_text,self.choice.choice_text)
    
class InfoPersonal(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    sucursal = models.CharField(default='',max_length=300)
    nombre = models.CharField(default='',max_length=300)
    puesto = models.CharField(default='', max_length=300)
    riesgos = models.CharField(default='',max_length=300 )
    correo = models.CharField(default='', max_length=300)
    




