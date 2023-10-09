from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, null=True,blank=True,default='@gmail.com')
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    dob = models.DateField()
    pix = models.ImageField(upload_to="profilepix")
    joined = models.DateField(auto_now_add=True)
    notification_read = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username