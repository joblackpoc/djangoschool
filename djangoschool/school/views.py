from django.shortcuts import render
from django.http import HttpResponse
from .models import ExamScore


def HomePage(request):
    #return HttpResponse('<h1>Hello world !!</h1>')
    return render(request,'school/home.html')


def AboutPage(request):
    return render(request,'school/about.html')


def ContactUs(request):
    return render(request,'school/contactus.html')    


def ShowScore(request):
    score = ExamScore.objects.all()
    context = {'score':score}

    return render(request,'school/showscore.html', context)













