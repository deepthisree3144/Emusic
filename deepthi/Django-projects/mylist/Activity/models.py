from django.db import models


# Create your models here.
class r_data(models.Model):
    Name=models.CharField(max_length=20,default="")
    Age=models.IntegerField(max_length=5,default="")
    Adress=models.CharField(max_length=50,default="")
    Contact=models.IntegerField(max_length=10,default="")
    Mail=models.CharField(max_length=50,default="")



