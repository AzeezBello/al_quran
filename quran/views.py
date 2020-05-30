from django.shortcuts import get_list_or_404, get_object_or_404, render
from quran.models import *


def index(request):
    suras = get_list_or_404(Sura)
    return render(request, 'quran/index.html', {'suras': suras})


def sura(request, sura_number, translation=1):
    sura = get_object_or_404(Sura, number=sura_number)
    ayas = sura.ayas.all()
    if translation:
        translations = sura.translations.filter(translation=translation)
        ayas = zip(ayas, translations)
    return render(request, 'quran/sura.html', {'sura': sura, 'ayas': ayas})


def aya(request, sura_number, aya_number, translation=1):
    sura = get_object_or_404(Sura, number=sura_number)
    aya = get_object_or_404(Aya, sura=sura, number=aya_number)
    translated_aya = get_object_or_404(TranslatedAya, aya=aya, translation=translation)
    words = aya.words.all()
    return render(request, 'quran/aya.html', {'sura': sura, 'aya': aya, 'translation': translated_aya, 'words': words})

