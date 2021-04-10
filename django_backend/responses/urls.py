from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from responses import views

urlpatterns = [
    path('list', views.SurveyResponseList.as_view()),
    # path('query', views.SurveyResponseList.as_view()),
    # re_path(r'^stores/(?P<store_id>\d+)/'),
]

urlpatterns = format_suffix_patterns(urlpatterns)