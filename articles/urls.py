from django.urls import path
from .views import articles, create_interview, open_interview, delete_interview, search_interview


urlpatterns = [
    path('', articles, name='articles'),
    path("create_interview", create_interview, name="create_interview"),
    path("<int:id>", open_interview, name="open_interview"),
    path("delete_interview/<int:id>", delete_interview, name="delete_interview"),
    path("find_interview", search_interview, name="find_interview"),
]