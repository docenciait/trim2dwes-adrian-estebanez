

from django.contrib.auth.models import User, Group  

from django.db import models  

.
class Account(models.Model):
    email = models.EmailField(unique=True)  
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  
    
    bio = models.TextField(max_length=500, blank=True)  
    date_of_birth = models.DateField(blank=True, null=True)  
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    
    
    groups = models.ManyToManyField(
        Group,
        related_name='account_groups',  
        blank=True  
    )

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']  

    def __str__(self):  
        
        return self.email 