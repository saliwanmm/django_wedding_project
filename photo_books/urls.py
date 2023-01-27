from django.urls import path
from .views import photo_books, story, photo_book_comment_crate, foto_photobook_daughter


urlpatterns = [
    path('', photo_books, name='photo_books'),
    path('<int:id>/<int:pk>', story, name='story'),
    path('<int:id>', photo_book_comment_crate, name='photo_book_comment_crate'),
    path('daughter/<int:id>/<int:pk>', foto_photobook_daughter, name='foto_photobook_daughter'),
]