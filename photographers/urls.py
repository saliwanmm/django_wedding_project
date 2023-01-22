from django.urls import path
from .views import photographers, foto_photographer


urlpatterns = [
    path('', photographers, name='photographers'),
    path('<int:id>/<int:pk>', foto_photographer, name='foto_photographer'),
]