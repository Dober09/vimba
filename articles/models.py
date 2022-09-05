from email.policy import default
from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # picture = models.ImageField(default='default.png',blank=True)
    
    def __str__(self):
        return self.name