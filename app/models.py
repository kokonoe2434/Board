from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    zipnumber = models.CharField(max_length=10, blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')
    good = models.IntegerField(blank=True, null=True, default=0)
    read = models.IntegerField(blank=True, null=True, default=0)
#    readMember = models.ForeignKey('ReadMember', on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ':' + str(self.pk)

class ReadMember(models.Model):
    boardModel = models.ForeignKey('BoardModel', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name