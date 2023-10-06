from django import forms

from app.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class StudentFrom(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


