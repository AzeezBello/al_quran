from django.urls import include, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='quran_index'),
    re_path(r'^(?P<sura_number>\d+)/$', views.sura, name='quran_sura'),
    re_path(r'^(?P<sura_number>\d+)/(?P<aya_number>\d+)/$', views.aya, name='quran_aya'),
    re_path(r'^(?P<sura_number>\d+)/(?P<aya_number>\d+)/(?P<word_number>\d+)/$', views.word, name='quran_word'),
    re_path(r'^lemma/(?P<lemma_id>\d+)/$', views.lemma, name='quran_lemma'),
    re_path(r'^root/(?P<root_id>\d+)/$', views.root, name='quran_root'),
    re_path(r'^root/$', views.root_index, name='quran_root_list'),
]


