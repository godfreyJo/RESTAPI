from django.shortcuts import render
from rest_framework import viewsets
from .models import Language

from .serializers import LanguageSerializer

class LanguageView(viewsets.ModelViewSet, Language):
    queryset = Language.objects.all()
    serializers_class = LanguageSerializer