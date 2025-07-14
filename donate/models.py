from django.db import models

# Create your models here.
class login(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=8)
    user_type=models.CharField(max_length=10)

class user(models.Model):
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    location=models.CharField(max_length=20)
    login_id=models.OneToOneField(login,on_delete=models.CASCADE,null=True,blank=True)

class donations(models.Model):
    food_name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    donation_status=models.CharField(max_length=50,default='pending')
    login_id=models.ForeignKey(login,on_delete=models.CASCADE,null=True,blank=True)

class requests(models.Model):
    donation_id=models.ForeignKey(donations,on_delete=models.CASCADE,null=True,blank=True)
    request_status=models.CharField(max_length=50,default='requested')
    ngo=models.ForeignKey(login,on_delete=models.CASCADE,null=True,blank=True)
    donor_id=models.ForeignKey(login,on_delete=models.CASCADE,null=True,blank=True,related_name='donr')