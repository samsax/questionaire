
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db import connection
from json import dumps
from polls.modules.fetchdb import dictfetchall

@login_required
def result_graph(request):
    template_name = 'covid_test/result_graph.html'
    return render(request, template_name)



def get_results(request):
    
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT(date_response) 
            FROM polls_responsecovid
            ORDER BY date_response ASC
        """)
        dates = dictfetchall(cursor)
    
    if(dates):
        categories = []
        series = [
            dict(name='Leves',data=[0] * len(dates)),
            dict(name='Graves',data=[0] * len(dates)),
            dict(name='Contacto',data=[0] * len(dates)),
            dict(name='Confirmados',data=[0] * len(dates))
        ]
        for row in dates:
            categories.append("{}".format(row['date_response']))
            index = 0
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT count(*)as count,question,choice_text
                FROM polls_responsecovid
                where date_response = '{}'
                GROUP BY question,choice_text
                """.format(row['date_response']))
                rows = dictfetchall(cursor)
                if(rows):
                    for row in rows:
                        series[question_to_row(row['question'])]['data'][index] = row['count']
                        index= index+1
            
        resp = dumps(dict(success=True,message = 'Obtenido',categories = categories, series=series))
    else:
        resp = dumps(dict(success=False,message = 'Error'))
    return HttpResponse(resp, content_type='application/json')


def question_to_row(question_id):
    if(question_id == 3):
        return 0
    elif(question_id == 1):
        return 2
    elif(question_id == 2):
        return 3
    else:
        return 1