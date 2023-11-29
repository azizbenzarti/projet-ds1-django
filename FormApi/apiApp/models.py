from django.db import models

class FormData(models.Model):
    name = models.CharField(max_length=255)
    hobbies = models.CharField(max_length=255)
    age = models.IntegerField()
    fieldOfStudy = models.CharField(max_length=255)

    def __str__(self):
        return self.name