from django.urls import path
from .views import photo_books, story, photo_book_comment_crate, foto_photobook_daughter, delete_comment_photobook, story_create, delete_story, delete_story_portfolio


urlpatterns = [
    path('', photo_books, name='photo_books'),
    path('<int:id>/<int:pk>', story, name='story'),
    path("story-create", story_create, name="story-create"),
    path('<int:id>', photo_book_comment_crate, name='photo_book_comment_crate'),
    path('daughter/<int:id>/<int:pk>', foto_photobook_daughter, name='foto_photobook_daughter'),
    path("delete_comment_photobook/<int:id>", delete_comment_photobook, name="delete_comment_photobook"),
    path("delete-story/<int:id>", delete_story, name="delete-story"),
    path("delete-story-portfolio/<int:id>", delete_story_portfolio, name="delete_story_portfolio"),
]