from django.db import models
from uuid import uuid4
from datetime import datetime

from django.urls import reverse
# Create your models here.

class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
    
    
class Price(models.Model):
    id = models.AutoField(primary_key=True)
    provider_id = models.ForeignKey(Provider, related_name="provider", on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, related_name="article", on_delete=models.CASCADE)
    price = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
