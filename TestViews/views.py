from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import viewsets
from TestViews.serializers import  PersonSerializer
from TestViews.models import Person



class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer