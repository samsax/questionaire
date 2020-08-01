from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views_steps import steps, result
from .web_services import response

app_name = 'polls'
urlpatterns = [
	# ex: /polls/
    path('register', views.register),
    path('login', views.login, name='login'),
    path('logout', views.logout),
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:questionnaire_id>/questionnaire_part/', views.questionnaire_part, name='questionnaire_part'),
    path('<int:questionnaire_id>/<int:part_id>/question_part/', views.question_part, name='question_part'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('covid/step1/', steps.step1, name='step1'),
    path('covid/step2/', steps.step2, name='step2'),
    path('covid/step3/', steps.step3, name='step3'),
    path('covid/step4/', steps.step4, name='step4'),
    path('covid/result/', result.result_graph, name='result_graph'),
    path('save_response', response.save_response, name='save_response'),
    path('save_response_covid', response.save_response_covid, name='save_response_covid'),
    path('save_response_info_personal', response.save_response_info_personal, name='save_response_info_personal'),
    path('select2', views.select2, name='select2'),
] + static( '/static/', document_root=settings.STATIC_ROOT, show_indexes=True )
