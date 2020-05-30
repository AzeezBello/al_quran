from django.contrib import admin
from .models import *


# Register your models here.
class SuraAdmin(admin.ModelAdmin):
    search_fields = ['number', 'tname', 'ename']
    list_display = ['number', 'tname', 'ename', 'name', 'type', 'order', 'rukus',]


class AyaAdmin(admin.ModelAdmin):
    search_fields = ['sura', 'number', 'arabic', ]
    list_display = ['sura', 'number', 'arabic', ]


class QuranTranslationAdmin(admin.ModelAdmin):
    pass


class TranslatedAyaAdmin(admin.ModelAdmin):
    search_fields = ['sura', 'aya', 'translation', 'english', ]
    list_display = ['sura', 'aya', 'translation', 'english', ]


admin.site.register(Sura, SuraAdmin)
admin.site.register(Aya, AyaAdmin)
admin.site.register(QuranTranslation, QuranTranslationAdmin)
admin.site.register(TranslatedAya, TranslatedAyaAdmin)
