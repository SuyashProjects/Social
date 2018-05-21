from django.db import models
from django.utils import timezone

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def submit(self):
        self.save()
    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to = 'static/', default = 'static/no-img.jpg')
    created_at = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes')
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(default=timezone.now)
    liked = models.BooleanField(default=False)

    def approve(self):
        self.liked = True
        self.save()

    def __str__(self):
        return self.created_date

class Dislike(models.Model):
    post = models.ForeignKey(Post, related_name='dislikes')
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(default=timezone.now)
    disliked = models.BooleanField(default=False)

    def approve(self):
        self.disliked = True
        self.save()

    def __str__(self):
        return self.created_date
