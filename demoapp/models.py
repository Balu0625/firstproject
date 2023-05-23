from django.db import models




# Create your models here.
class Diary(models.Model):
    diary=models.TextField()
    date=models.CharField(max_length=30)
    time=models.CharField(max_length=30)
    day=models.CharField(max_length=30)

    def __str__(self):
        return self.diary
    


class Todo(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)