from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Employee(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name
