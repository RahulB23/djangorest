from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=64)
    user_pass = models.CharField(max_length=64)

    def __str__(self):
        return self.user_name

class Book(models.Model):
    book_name = models.CharField(max_length=64)
    book_quant = models.IntegerField(default=0)
    author = models.CharField(max_length=64)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.book_name
