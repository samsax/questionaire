import json 
from json import dumps
from django.http import HttpResponse
from polls.models import Choice, Question, Questionnaire, QuestionnairePart, PartQuestion, Response
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