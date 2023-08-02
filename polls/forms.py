from django import forms

from .models import Question, Choice


class AddPollForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        widgets = {'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})}

class AddChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']