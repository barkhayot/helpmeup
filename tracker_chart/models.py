from django.db import models
from django.contrib.auth.models import User



class testCHART(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    chart_name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.chart_name


class testCHART_DATA(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    chart = models.ForeignKey(testCHART, on_delete=models.CASCADE)
    data_name = models.CharField(max_length=50)
    data = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data_name

