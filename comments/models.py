from django.db import models

# Create your models here.

class Comment(models.Model):
    description = models.CharField(max_length=256)
    amiibo_id = models.IntegerField()
    user_id = models.IntegerField()

    def __str__(self):
        return self.description
