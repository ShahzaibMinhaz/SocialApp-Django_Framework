from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to="profile_pics")

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    postText = models.CharField(max_length=100)
    postImage = models.ImageField(upload_to="post_pics")
    postLikes = models.ManyToManyField(profile)

    def __str__(self):
        return self.postText

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    commentText = models.CharField(max_length=50)
