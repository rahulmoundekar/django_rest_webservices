from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from orm_onetoone_rest_curd_app.models import Person, License
from orm_onetoone_rest_curd_app.serializers import PersonSerializer, LicenseSerializer


class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    print(queryset)


class LicenseView(viewsets.ModelViewSet):
    serializer_class = LicenseSerializer
    queryset = License.objects.all()
