from django.urls import path
from .views import portfolio, portfolio_comment_delete
from . import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<int:id>/<int:pk>', views.foto_portfolio, name='foto_portfolio'),
    path('comment_create/<int:id>', views.portfolio_comment_crate, name='portfolio_comment_crate'),
    path("portfolio_comment_delete/<int:id>", portfolio_comment_delete, name="portfolio_comment_delete"),
]