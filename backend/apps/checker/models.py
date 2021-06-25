from django.db import models


class ArticleExample(models.Model):
    body_text = models.TextField()
    # This bias score is a left-right bias provided by Media Bias Chart
    bias_score = models.FloatField()
    bias_class = models.IntegerField()
    quality_score = models.FloatField()
    # quality_class is based on the quality score and allows us to
    # integrate politifact data in their
    # 4-class way, True = 4, Mostly True = 3, Mostly Fake = 2,
    # Fake = 1
    quality_class = models.IntegerField()

    origin_url = models.TextField()
    origin_source = models.TextField()


class DictEntry(models.Model):
    canonWord = models.TextField()


class UserEntry(models.Model):
    entryURL = models.URLField(verbose_name='URL of news article')
