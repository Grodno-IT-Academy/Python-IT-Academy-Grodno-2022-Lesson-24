from django.forms import ModelForm, Form, CharField
from .models import Question, Choice

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']

class SarchForm(Form):
    query = CharField()