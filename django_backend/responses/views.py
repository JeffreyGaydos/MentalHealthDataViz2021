from responses.models import SurveyResponse
from responses.serializers import SurveyResponseSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SurveyResponseList(APIView):
    
    def get(self, request, format=None):
        responses = SurveyResponse.objects.all()
        serializer = SurveyResponseSerializer(responses, many=True)
        return Response(serializer.data)
