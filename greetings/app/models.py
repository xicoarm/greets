from django.db import models

# Create your models here.

class PreOrder(models.Model):

    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=254, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    recipient = models.TextField(null=True)
    category = models.TextField(null=True)
    text_length = models.TextField(null=True)
    unique_term = models.TextField(null=True)
    unique_id = models.TextField(null=True)
    already_sent = models.BooleanField(null = True, blank=True)

class Order(models.Model):

    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=254, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    recipient = models.TextField(null=True)
    category = models.TextField(null=True)
    text_length = models.TextField(null=True)
    unique_term = models.TextField(null=True)
    unique_id = models.TextField(null=True)