from django.urls import path
from .views import portfolio
from . import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
]