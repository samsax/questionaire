
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

def result_graph(request):
    if request.user.is_authenticated:
        template_name = 'covid_test/result_graph.html'
        return render(request, template_name)
    else:
        return redirect('/polls/login')