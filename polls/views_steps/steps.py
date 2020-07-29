
from django.shortcuts import get_object_or_404, render, redirect

def step2(request):
    template_name = 'covid_test/step2.html'
    return render(request, template_name)

def step3(request):
    template_name = 'covid_test/step3.html'
    return render(request, template_name)

def step4(request):
    template_name = 'covid_test/step4.html'
    return render(request, template_name)