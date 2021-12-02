from django.db import models


# Create your models here.
class Comments(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    animes = models.ForeignKey('anime.Anime', on_delete=models.CASCADE)
    comments = models.CharField(max_length=1000)
