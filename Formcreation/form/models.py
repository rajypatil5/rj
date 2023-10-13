from django.db import models

# Create your models here.
class registrationModel(models.Model):
    options=(('ST','Student'),('EM','Employee'))
    Designation=models.CharField(max_length=2,choices=options)
    Name=models.CharField(max_length=25)
    Email=models.EmailField()
    Mobile=models.IntegerField()