from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
  bio = models.TextField(null=True)
  company_name = models.TextField(null=True)
 


class Wishlist(models.Model):
  user_id = models.IntegerField()
  product_id = models.IntegerField()