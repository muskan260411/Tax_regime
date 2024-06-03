from django.db import models

from django.contrib.auth.models import AbstractUser,  Group, Permission

class CustomUser(AbstractUser):
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=True)
    employee_id= models.CharField(max_length=50, unique=True)
    groups = models.ManyToManyField(Group, related_name='customuser_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions', blank=True)
    def __str__(self):
        return self.username
    
class TaxRegime(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    regime_choice = models.CharField(max_length=20, choices=[('New', 'New Tax Regime'), ('Old', 'Old Tax Regime')], default='New')


