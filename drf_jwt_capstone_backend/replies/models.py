from django.db import models

# Create your models here.
class Replies(models.Model):
    comments = models.ForeignKey('comments.Comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)