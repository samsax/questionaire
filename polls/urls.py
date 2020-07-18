from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .web_services import response
app_name = 'polls'
urlpatterns = [
	# ex: /polls/
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:questionnaire_id>/questionnaire_part/', views.questionnaire_part, name='questionnaire_part'),
    path('<int:part_id>/question_part/', views.question_part, name='question_part'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('save_response', response.save_response, name='save_response'),
    path('select2', views.select2, name='select2'),
] + static( '/static/', document_root=settings.STATIC_ROOT, show_indexes=True )