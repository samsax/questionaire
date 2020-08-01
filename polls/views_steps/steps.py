
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

def step1(request):
    if request.user.is_authenticated:
        template_name = 'covid_test/step1.html'
        return render(request, template_name)
    else:
        return redirect('/polls/login')

def step2(request):
    if request.user.is_authenticated:
        template_name = 'covid_test/step2.html'
        return render(request, template_name)
    else:
        return redirect('/polls/login')

def step3(request):
    if request.user.is_authenticated:
        template_name = 'covid_test/step3.html'
        return render(request, template_name)
    else:
        return redirect('/polls/login')

def step4(request):
    if request.user.is_authenticated:
        template_name = 'covid_test/step4.html'
        return render(request, template_name)
    else:
        return redirect('/polls/login')