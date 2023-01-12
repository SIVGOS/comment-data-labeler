from django.db import models
from django.contrib.auth.models import User
class Labels(models.Model):
    label_text = models.CharField(max_length=64, unique=True)
    display_text = models.CharField(max_length=64)

class Comment(models.Model):
    video_id = models.CharField(max_length=16)
    topic = models.CharField(max_length=32)
    channel_title = models.CharField(max_length=32)
    video_title = models.CharField(max_length=128)
    comment_id = models.CharField(max_length=32)
    comment_text = models.TextField()
    labels = models.ManyToManyField(Labels)

class LabellerMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    label = models.ForeignKey(Labels, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
