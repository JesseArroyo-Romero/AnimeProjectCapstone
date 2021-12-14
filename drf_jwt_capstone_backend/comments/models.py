from django.db import models


# Create your models here.
class Comments(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    anime_id = models.IntegerField(default=0)
    comments = models.CharField(max_length=1000)
