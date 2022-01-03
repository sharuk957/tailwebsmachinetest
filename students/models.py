from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Subject(models.Model):
    subject = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=CASCADE)

    def __str__(self):
        return self.subject


class Student(models.Model):

    subject = models.ForeignKey(Subject,on_delete=CASCADE)
    name = models.CharField(max_length=250)
    mark = models.IntegerField()
    user = models.ForeignKey(User,on_delete=CASCADE)

    def __str__(self):
        return self.name