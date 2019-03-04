from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'd_article'
