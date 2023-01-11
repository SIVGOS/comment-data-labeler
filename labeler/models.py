from django.db import models

class Comment(models.Model):
    video_id = models.CharField(max_length=16)
    topic = models.CharField(max_length=32)
    channel_title = models.CharField(max_length=32)
    video_title = models.CharField(max_length=128)
    comment_id = models.CharField(max_length=32)
    comment_text = models.TextField()
    tags = models.CharField(max_length=64, null=True)
