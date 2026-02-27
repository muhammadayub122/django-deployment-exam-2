from django.db import models

# Create your models here.
class Student(models.Model):
    ism=models.CharField(max_length=55)
    bio=models.TextField(blank=True,null=True)
    yosh=models.SmallIntegerField(default=0)
    
    def __str__(self):
        return f"{self.ism}"