from django.urls import path
from .views import home
from . import views
from portfolio.views import portfolio_comment_crate


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
    path('delete/<int:id>', views.delete_foto, name='delete_foto'),
    path('comment_create/<int:id>', portfolio_comment_crate, name='portfolio_comment_crate'),
]