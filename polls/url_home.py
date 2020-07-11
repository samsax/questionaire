from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
	# ex: /polls/
    path('', views.home)
    
] + static( '/static/', document_root=settings.STATIC_ROOT, show_indexes=True )