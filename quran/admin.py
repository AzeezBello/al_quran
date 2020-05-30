from django.contrib import admin
from .models import *


# Register your models here.
class SuraAdmin(admin.ModelAdmin):
    search_fields = ['number', 'tname', 'ename']
    list_display = ['number', 'tname', 'ename', 'name', 'type', 'order', 'rukus',]


class AyaAdmin(admin.ModelAdmin):
    search_fields = ['sura', 'number', 'text', ]
    list_display = ['sura', 'number', 'text', ]


class QuranTranslationAdmin(admin.ModelAdmin):
    pass


class TranslatedAyaAdmin(admin.ModelAdmin):
    search_fields = ['sura', 'aya', 'translation', 'text', ]
    list_display = ['sura', 'aya', 'translation', 'text', ]


class RootAdmin(admin.ModelAdmin):
    pass


class LemmaAdmin(admin.ModelAdmin):
    pass


class WordAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sura, SuraAdmin)
admin.site.register(Aya, AyaAdmin)
admin.site.register(QuranTranslation, QuranTranslationAdmin)
admin.site.register(TranslatedAya, TranslatedAyaAdmin)
admin.site.register(Root, RootAdmin)
admin.site.register(Lemma, LemmaAdmin)
admin.site.register(Word, WordAdmin)
