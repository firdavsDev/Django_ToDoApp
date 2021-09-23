from django.db import models

# Create your models here.
class Vazifa(models.Model):
    mavzu=models.CharField(max_length=200)
    tugadi=models.BooleanField(default=False)
    yaratish=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.mavzu