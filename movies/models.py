from django.db import models
import uuid
from customer.models import AGE_CHOICE

# Create your models here.

MOVIE_CHOICE=(
    ('seasonal','seasonal'),
    ('single','single')
)
class Movies(models.Model):
    title = models.TextField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(choices=MOVIE_CHOICE,max_length=10)
    video = models.ManyToManyField('videos')
    image = models.ImageField(upload_to='cover')
    agel_limit = models.CharField(choices=AGE_CHOICE,max_length=15)
    def __str__(self) -> str:
        return self.title

class videos(models.Model):
    title=models.CharField(max_length=100)
    file=models.FileField(upload_to='movies') 
    def __str__(self) -> str:
        return self.title   