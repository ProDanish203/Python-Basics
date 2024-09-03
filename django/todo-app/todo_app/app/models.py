from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # images
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.title


# Relationship
# One to Many
class TodoReview(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} review for {self.todo.title}"


# Many to Many
class Category(models.Model):
    name = models.CharField(max_length=200)
    todos = models.ManyToManyField(Todo, related_name="categories")

    def __str__(self):
        return self.name

# One to One
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(upload_to="profile_images/", null=True, blank=True)

    def __str__(self):
        return self.user.username

