from django import forms
from app01 import models
from django.forms import ModelForm,TextInput,Select


class QuestionModelForm(ModelForm):
    class Meta:
        model = models.Question
        fields = ['caption','tp']
        error_messages = {
            'caption': {'required': '名称不能为空', 'invalid': '格式错误'}
        }
        widgets = {
            'caption': TextInput(attrs={'class': 'form-control'}),
            'tp':Select(attrs={'class': 'form-control'})
        }


class OptionModelForm(ModelForm):
    class Meta:
        model = models.Option
        fields = ['name','score']
