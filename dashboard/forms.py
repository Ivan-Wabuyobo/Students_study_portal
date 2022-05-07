from django.forms import ModelForm, DateInput
from .models import *
from django.contrib.admin import widgets

class Create_notes(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

class DateInput(DateInput):
    input_type = 'date'

class Create_homework(ModelForm):
    class Meta:
        model = Homework
        widgets = {'due': DateInput()}
        fields =['subject','title', 'description', 'due']
  

