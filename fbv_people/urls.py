from django.urls import path

from .views import people_list, person_detail

urlpatterns = [
    path("people/", people_list),
    path("person/<int:pk>/", person_detail)
]
