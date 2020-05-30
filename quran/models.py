from django.db import models


class Sura(models.Model):
    """Sura (chapter) of the Quran"""

    REVELATION_CHOICES = (
        ('Meccan', 'Meccan'),
        ('Medinan', 'Medinan'),
    )

    number = models.IntegerField(primary_key=True, verbose_name='Sura Number')
    name = models.CharField(max_length=50, verbose_name='Sura Name')
    tname = models.CharField(max_length=50, verbose_name='English Transliterated Name')
    ename = models.CharField(max_length=50, verbose_name='English Name')
    order = models.IntegerField(verbose_name='Revelation Order')
    type = models.CharField(max_length=7, choices=REVELATION_CHOICES, verbose_name='')
    rukus = models.IntegerField(verbose_name='Number of Rukus')
    bismillah = models.CharField(max_length=50, blank=True, verbose_name='Bismillah')

    class Meta:
        ordering = ['number']

    def __str__(self):
        return self.tname

    def __unicode__(self):
        return self.tname


class Aya(models.Model):
    """Aya (verse) of the Quran"""

    number = models.IntegerField(verbose_name='Aya Number')
    sura = models.ForeignKey(Sura, on_delete=models.CASCADE, related_name='ayas', db_index=True)
    arabic = models.TextField(blank=False)

    class Meta:
        unique_together = ('number', 'sura')
        ordering = ['sura', 'number']

    def __str__(self):
        return str(self.number)


class QuranTranslation(models.Model):
    """Metadata relating to a translation of the Quran"""
    name = models.CharField(blank=False, max_length=50)
    translator = models.CharField(blank=False, max_length=50)
    source_name = models.CharField(blank=False, max_length=50)
    source_url = models.URLField(blank=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class TranslatedAya(models.Model):
    """Translation of an aya"""
    sura = models.ForeignKey(Sura, on_delete=models.CASCADE, related_name='translations', db_index=True)
    aya = models.ForeignKey(Aya, on_delete=models.CASCADE, related_name='translations', db_index=True)
    translation = models.ForeignKey(QuranTranslation, on_delete=models.CASCADE, db_index=True)
    english = models.TextField(blank=False)
    transliteration = models.TextField(blank=True)

    class Meta:
        unique_together = ('aya', 'translation')
        ordering = ['aya']

    def __unicode__(self):
        return self.english

    def __str__(self):
        return self.english

