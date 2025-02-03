from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Person
from .serializers import PersonSerializer


class PeopleList(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
