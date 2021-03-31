from django.shortcuts import render
from .models import quiz
from django.http import HttpResponse
from django.contrib import messages
quiz_data=quiz.objects.all()

def index(request,k=0):
    request.session['answered_correctly']=0       
    return render(request,"quiz/index.html",{"number":1,"data":quiz_data[0]})

def nextQuestion(request,k):
    if request.method == "POST":
        if request.POST.get('option')==quiz_data[k-1].correct:
            request.session['answered_correctly']+=1
    if k==6:
        return render(request,"quiz/score.html",{"correct":request.session['answered_correctly'],"total":6})
    return render(request,"quiz/index.html",{"number":k+1,"data":quiz_data[k]})