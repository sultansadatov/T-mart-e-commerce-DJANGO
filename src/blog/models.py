from django.db import models
from datetime import date

# Create your models here.

class Comments(models.Model):
    comment_text = models.TextField()
    comment_at = models.DateField()
    subject = models.CharField(max_length=255)

class Blog(models.Model):
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    header = models.CharField(max_length=66)
    description = models.TextField()
    created_at = models.DateField()
    Comments_id = models.ForeignKey(Comments, on_delete=models.CASCADE)

    def main_image(self):
        return self.images.all()[0]    
          

class Tags(models.Model):
    tag_name = models.CharField(max_length=100)
    blog = models.ManyToManyField("blog.Blog")


class Media(models.Model):
    blog_id = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE, related_name="images")
    media = models.FileField(upload_to="uploads/%Y/%m/%d/", null=True)
    is_main = models.BooleanField(default=False)