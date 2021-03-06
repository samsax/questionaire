
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from polls.models import InfoPersonal

@login_required
def step1(request):
    infoPersonal = InfoPersonal.objects.filter(
        user = request.user
    )
    print(infoPersonal)
    if not infoPersonal:
        template_name = 'covid_test/step1.html'
        return render(request, template_name)
    else:
        return redirect(reverse('polls:step2'))

@login_required    
def step2(request):
    template_name = 'covid_test/step2.html'
    return render(request, template_name)

@login_required
def step3(request):
    template_name = 'covid_test/step3.html'
    return render(request, template_name)
    
@login_required
def step4(request):
    template_name = 'covid_test/step4.html'
    return render(request, template_name)
    