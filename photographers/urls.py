from django.urls import path
from .views import photographers
# from .views import phone_card


urlpatterns = [
    path('', photographers, name='photographers'),
    # path('phone/<int:id>', phone_card, name="phone_card"),
]