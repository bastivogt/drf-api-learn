from django.urls import path

from .views import PeopleList, PersonDetail

urlpatterns = [
    path("people/", PeopleList.as_view()),
    path("person/<int:pk>/", PersonDetail.as_view())
]
