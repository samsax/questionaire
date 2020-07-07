from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
	# ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:questionnaire_id>/questionnaire_part/', views.questionnaire_part, name='questionnaire_part'),
    path('<int:part_id>/question_part/', views.question_part, name='question_part'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]