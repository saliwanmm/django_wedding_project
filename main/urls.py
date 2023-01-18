from django.urls import path
from .views import home
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('about', views.about, name='about'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('logout', views.logout_view, name='logout'),
    path('update/<int:id>', views.update_user, name='update_user'),
    path('change_password/<int:id>', views.change_password, name='change_password'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('personal_data/<int:id>', views.personal_data, name='personal_data'),
    path('personal_data_update/<int:id>', views.personal_data_update, name='personal_data_update'),
    path('profile/<int:id>/<int:pk>', views.foto_profile, name='foto_profile'),
]