from django.db import models

# Create your models here.
class Subscription(models.Model):
    email = models.EmailField(max_length=255)
    

class Staff(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.TextField()
    twitter_url = models.CharField(max_length=255)
    facebook_url = models.CharField(max_length=255)
    instagram_url = models.CharField(max_length=255)
    website_url = models.CharField(max_length=255)
    email = models.CharField(max_length=100)

class Contact(models.Model):
    your_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=100)
    message =  models.TextField()



class BlockedIp(models.Model):
    ip_adres = models.CharField(max_length = 15)

    def __str__(self):
        return self.ip_adres