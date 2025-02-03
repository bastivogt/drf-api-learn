from django.urls import path

from .views import AuthorList, AuthorDetail, BookList, BookDetail

urlpatterns = [
    path("author/", AuthorList.as_view()),
    path("author/<int:pk>/", AuthorDetail.as_view()),
    path("book/", BookList.as_view()),
    path("book/<int:pk>/", BookDetail.as_view())
]
