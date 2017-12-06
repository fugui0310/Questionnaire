from django.shortcuts import render, redirect, HttpResponse

from app01 import models
from django import forms
from django.forms import widgets,ValidationError

# Create your views here.



def index(request):
    questionnaire_list = models.Questionnaire.objects.all()
    return render(request, "index.html",locals())

class QuestionnaireForm(forms.Form):
    pass


def questionnaire(request,id):

    question_list = models.Question.objects.filter(questionnaire_id=id).all()




    return render(request,"questionnaire.html",locals())

def delete(request,id):
    models.Question.objects.filter(questionnaire_id=id).delete()



    return redirect("/questionnaire/")