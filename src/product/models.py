from django.db import models
from datetime import date
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.

class Reviews(models.Model):
    review_text = models.TextField()
    reviewed_at = models.DateField()
    rating = models.IntegerField()
    


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name



class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name



class Category(models.Model):
    title = models.CharField(verbose_name="Title",max_length=30, help_text="Max 30 char.")
    img = models.ImageField(upload_to='category/',default = 'empty',null = True, blank =True)
    parent = models.ForeignKey('self', verbose_name="Parent", on_delete=models.CASCADE,null=True, blank=True, default="", related_name="parent_category")
    is_navbar = models.BooleanField(default=True)
    child = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def _str_(self) -> str:
        return self.title




class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True, unique= True)
    def str(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)



class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name









class Product(models.Model):
    product_name = models.CharField(max_length=255)
    # old_price = models.IntegerField()
    price = models.IntegerField()
    product_info = models.TextField()
    product_description = models.TextField()
    product_detail = models.TextField()
    delivery_info= models.TextField()
    brand_id = models.ForeignKey(Brand, related_name="names", on_delete=models.CASCADE)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    reviews_id = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, related_name="names", on_delete=models.CASCADE)
    size_id = models.ForeignKey(Size, related_name="names", on_delete=models.CASCADE)

    def main_image(self):
        return self.images.all()[0]    
          
  

class Product1(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    #digital = models.BooleanField(default=False,null=True, blank=False)
    image = models.ImageField(null=True,blank=True)
    #id=models.CharField(max_length=100, null=True)
    
    def _str_(self):
        return self.id

    @property 
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url 

class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    total_amount = models.IntegerField()



class Media(models.Model):
    product_id = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name="images")
    media = models.FileField(upload_to="uploads/%Y/%m/%d/", null=True)
    is_main = models.BooleanField(default=False)