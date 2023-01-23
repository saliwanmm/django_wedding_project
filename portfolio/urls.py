from django.urls import path
from .views import portfolio
from . import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<int:id>/<int:pk>', views.foto_portfolio, name='foto_portfolio'),
    path('comment_create/<int:id>', views.portfolio_comment_crate, name='portfolio_comment_crate'),
]