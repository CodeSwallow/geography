from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

app_name = 'countries'
urlpatterns = [
    path('', main, name='index'),
    path('<int:pk>', main, name='index'),
    path('countries', CountryList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
