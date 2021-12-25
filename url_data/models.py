from django.db import models
from django.contrib.auth.models import User



class URL_DATA(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title