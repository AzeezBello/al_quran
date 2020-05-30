from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='quran_index'),
    re_path(r'^(?P<sura_number>\d+)/$', views.sura, name='quran_sura'),
    re_path(r'^(?P<sura_number>\d+)/(?P<aya_number>\d+)/$', views.aya, name='quran_aya'),
]


