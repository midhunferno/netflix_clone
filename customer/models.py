from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

AGE_CHOICE=(
    ('All','All'),
    ('Kids','Kids'),    
)

class CustomUser(AbstractUser):
    profile=models.ManyToManyField('profile',blank=True)
    conform_password=models.TextField()

    def __str__(self) -> str:
        return self.username

class Profile(models.Model):
    name=models.CharField(max_length=30)
    age_limit=models.CharField(choices=AGE_CHOICE,max_length=30)
    uuid=models.UUIDField(default=uuid.uuid4)

    def __str__(self) -> str:
        return self.name
    