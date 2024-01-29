from django.db import models

# Create your models here.
class gympaln(models.Model):
    plan=models.CharField(max_length=200)
    fee=models.IntegerField(default=True)

    def __str__(self) :
        return self.plan
    
class memeber(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    plan=models.ForeignKey(gympaln,on_delete=models.CASCADE)
    phonenumber=models.CharField(max_length=12)
    date = models.DateField()

    def __str__(self) :
        return self.name
    
class enquries(models.Model):
    name=models.CharField(max_length=200)
    conatct=models.IntegerField()
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=200)
    description=models.CharField(max_length=500,default='Not solve')

class equipments(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    weight=models.CharField(max_length=10)
    description=models.TextField(max_length=300)
    image = models.ImageField(upload_to='static/images/', null=False, blank=False,default='equipments2')

    def __str__(self):
        return(self.name)
    
