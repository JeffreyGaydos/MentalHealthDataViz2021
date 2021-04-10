from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from responses import views

urlpatterns = [
    path('list', views.SurveyResponseList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)