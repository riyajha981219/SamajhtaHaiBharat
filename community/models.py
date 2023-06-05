from django.db import models
from India.models import *
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(Member,blank=True,on_delete=models.CASCADE,related_name="poster")
    community=models.ForeignKey(Map,blank=True,on_delete=models.CASCADE,related_name="group")
    postpic= models.ImageField(blank=True)
    status=models.TextField()
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.status}"

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post")
    commenter = models.ForeignKey(Member,blank=True,on_delete=models.CASCADE,related_name="commenters",default="")
    comment=models.TextField(null=False)
    
    def __str__(self):
        return f"{self.comment}"

