
from django.db import models

# Create your models here.
class rooms(models.Model):
    img=models.ImageField(upload_to='pic')
    img1=models.ImageField(upload_to='pic')
    img2=models.ImageField(upload_to='pic')
    img3=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=200)
    des=models.TextField()
    timings=models.CharField(max_length=200)
    price=models.FloatField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

#comments class
class comment(models.Model):
    service=models.ForeignKey(rooms,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    body=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


#contact as 
class contactus(models.Model):
    name=models.CharField(max_length=200)
    mail=models.EmailField()
    phone=models.CharField(max_length=100)
    msg=models.TextField()
    def __str__(self):
        return self.name


#for print page
class printpage(models.Model):
    booking=models.CharField(max_length=200)
    inv=models.CharField(max_length=100)
    urname=models.CharField(max_length=100)
    checkin=models.CharField(max_length=100)
    checkot=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    def __str__(self):
        return self.urname

