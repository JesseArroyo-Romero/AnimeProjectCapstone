from django.db import models


# Create your models here.
class Anime(models.Model):
    comment = models.ForeignKey('comments.Comments', on_delete=models.CASCADE)
    replies = models.ForeignKey('replies.Replies', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    airing = models.BooleanField(default=False)
    synopsis = models.CharField(max_length=2000)
    type = models.CharField(max_length=50)
    episodes = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    rated = models.CharField(max_length=50)