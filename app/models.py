from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def submit(self):
        self.save()
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author = models.CharField(max_length=200)
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
