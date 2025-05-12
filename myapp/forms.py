# from django import forms
# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your Name', max_length=100)

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']