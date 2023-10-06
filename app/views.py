from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.forms import * 

def insert_course(request):
    CFO = CourseForm()
    d={'CFO':CFO}
    if request.method == 'POST':
        CFDO = CourseForm(request.POST)
        if CFDO.is_valid():
            CFDO.save()
            return HttpResponse('<center><h1 style="color: green;">Data inserted successfully</h1></center>')
    return render(request,'insert_course.html',d)

def insert_student(request):
    SFO = StudentFrom()
    d={'SFO':SFO}
    if request.method == 'POST':
        SFDO = StudentFrom(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('<center><h1 style="color: green;">Data inserted successfully</h1></center>')
    return render(request,'insert_student.html',d)