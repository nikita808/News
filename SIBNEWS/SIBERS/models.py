from django.db import models


class News(models.Model):
    headline = models.CharField(max_length=120, null=False, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField()
    pic_src_link = models.CharField(max_length=240, blank=True)
