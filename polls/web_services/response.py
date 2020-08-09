import json 
from json import dumps
from django.http import HttpResponse
from polls.models import Choice, Question, Questionnaire, QuestionnairePart, PartQuestion, Response, ResponseCovid,InfoPersonal
def save_response(request):
    if request.method == "POST":
        body = json.loads(request.body)
        many_response = (json.loads(body['data']['data']))
        print(many_response)
        for question_id in many_response:
            question = Question.objects.filter(id = question_id)
            if(question):
                question = question[0]
                if(question.question_type in [1,2]):
                    response = Response(
                        question = question,
                        choice_text = many_response[question_id]
                    )
                    response.save()
                else:
                    for response_text in  many_response[question_id]:
                        response = Response(
                            question = question,
                            choice_text = response_text
                        )
                        response.save()
                
    resp = dumps(dict(success=True,message = 'Guardado'))
    return HttpResponse(resp, content_type='application/json')


def save_response_covid(request):
    if request.method == "POST":
        body = json.loads(request.body)
        many_response = (json.loads(body['data']['data']))
        print(many_response)
        for question_id in many_response:
            if(isinstance(many_response[question_id], list)):
                choice_value = evaluate_response(question_id, many_response[question_id])
                print(choice_value)
                for response_text in  many_response[question_id]:
                    response = ResponseCovid(
                        user=request.user,
                        question = question_id,
                        choice_text = response_text,
                        choice_value = choice_value
                    )
                    response.save()
            else:
                response = ResponseCovid(
                    user=request.user,
                    question = question_id,
                    choice_text = many_response[question_id],
                    choice_value = evaluate_response(question_id, many_response[question_id])
                )
                response.save()
                
        resp = dumps(dict(success=True,message = 'Guardado'))
        return HttpResponse(resp, content_type='application/json')

def save_response_info_personal(request):
    if request.method == "POST":
        body = json.loads(request.body)
        many_response = (json.loads(body['data']['data']))
        print(many_response)
        response = InfoPersonal(
            user=request.user,
            sucursal=  many_response['1'],
            nombre= many_response['2'],
            correo=  many_response['3'],
            puesto=  many_response['4'],
            riesgos= many_response['5'],
        )
        response.save()
        resp = dumps(dict(success=True,message = 'Guardado'))
        return HttpResponse(resp, content_type='application/json')

def evaluate_response(question, choice_text):
    question = int(question)
    if(question==1):
        if "No" not in choice_text: 
            return 1
        else:
            return 0
    elif(question in [2,3,5]):
        if(choice_text=='Sí'):
            return 1
        else:
            return 0
    else:
        return 0
    
    
        