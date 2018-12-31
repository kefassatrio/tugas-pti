from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Friends(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    tempat_tanggal_lahir = models.CharField(default='', max_length=500)
    description = models.TextField(default='')
    line = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.name

    def snippet(self):
        if len(self.description) > 20:
            return self.description[:20] + "..."
        else:
            return self.description

    class Meta:
        verbose_name_plural = "friends"

class Comment(models.Model):
    friend = models.ForeignKey(Friends, default='', on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    username = models.ForeignKey(User, default=None, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(default=None)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
