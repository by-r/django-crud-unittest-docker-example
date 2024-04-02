from django.db import models

# Create your models here.
class Todolist(models.Model):

    title = models.CharField(max_length=50)
    desc = models.TextField()
    isdone = models.BooleanField()

    def __str__(self):
        return self.title
    