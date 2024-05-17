from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
AGE_CHOICE=(
    ('All','All'),
    ('Kids','Kids'),    
)
class Costom (AbstractUser):
    profile=models.ManyToManyField('profile',blank=True)
