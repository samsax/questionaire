import json 
from django.http import HttpResponse
def save_response(request):
    if request.method == "POST":
        print(request.body)
    resp = {}
    return HttpResponse(resp, content_type='application/json')