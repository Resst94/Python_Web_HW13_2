from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    fullname = models.CharField(max_length=64, null=False, unique=True)
    born_date = models.CharField(max_length=64)
    born_location = models.CharField(max_length=256)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Tag(models.Model):
    name = models.CharField(max_length=60, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Tags"
        verbose_name = "Tag"

    def __str__(self):
        return self.name


class Quote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
