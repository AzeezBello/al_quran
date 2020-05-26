from django.contrib import admin
from .models import *


# Register your models here.
class SuraAdmin(admin.ModelAdmin):
    pass


class AyaAdmin(admin.ModelAdmin):
    pass


class QuranTranslationAdmin(admin.ModelAdmin):
    pass


class TranslatedAyaAdmin(admin.ModelAdmin):
    pass


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
