from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .web_services import response
from .views_steps import steps
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
    path('<int:questionnaire_id>/<int:part_id>/question_part/', views.question_part, name='question_part'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('covid/step2/', steps.step2, name='step2'),
    path('covid/step3/', steps.step3, name='step3'),
    path('covid/step4/', steps.step4, name='step4'),
    path('save_response', response.save_response, name='save_response'),
    path('select2', views.select2, name='select2'),
] + static( '/static/', document_root=settings.STATIC_ROOT, show_indexes=True )