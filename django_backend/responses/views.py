from responses.models import SurveyResponse
from responses.serializers import SurveyResponseSerializer, SurveyResponseAgeDepressionSerializer
from django.http import Http404
from rest_framework.views import APIView
from django.views import generic
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend


class SurveyResponseList(generics.ListAPIView):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseAgeDepressionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['race', 'born_year', 'gender']
    
