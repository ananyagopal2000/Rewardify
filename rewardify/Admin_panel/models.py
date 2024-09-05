from django.db import models

class App(models.Model):
    app_name=models.CharField(max_length=50)
    download_link = models.URLField()
    points = models.IntegerField()