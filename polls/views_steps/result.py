
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def result_graph(request):
    template_name = 'covid_test/result_graph.html'
    return render(request, template_name)
    