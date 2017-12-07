from django.shortcuts import render, redirect, HttpResponse

from app01 import models, forms
import json
# from django import forms
from django.forms import widgets, ValidationError


# Create your views here.



def index(request):
    questionnaire_list = models.Questionnaire.objects.all()
    return render(request, "index.html", locals())


def questionnaire(request,id):
    def inner():
        question_list = models.Question.objects.filter(questionnaire_id=id).all()  # [Question,Question,Question]
        if not question_list:
            # 新创建的问卷，其中还么有创建问题
            form = forms.QuestionModelForm()
            yield {'form': form, 'obj': None, 'option_class': 'hide', 'options': None}
        else:
            for que in question_list:
                form = forms.QuestionModelForm(instance=que)
                temp = {'form': form, 'obj': que, 'option_class': 'hide', 'options': None}
                if que.tp == 2:
                    temp['option_class'] = ''

                    # 获取当前问题的所有选项？que
                    def inner_loop(quee):
                        option_list = models.Option.objects.filter(qs=quee)
                        for v in option_list:
                            yield {'form': forms.OptionModelForm(instance=v), 'obj': v}

                    temp['options'] = inner_loop(que)


                yield temp

    return render(request, "questionnaire.html", {'question_list': inner()})


# def delete(request, id):
#     models.Question.objects.filter(questionnaire_id=id).delete()
#
#     return redirect("/questionnaire/")

def submit_que(request):
    data = json.loads(request.body.decode('utf8'))
    print(data)
    return render(request,'questionnaire.html')