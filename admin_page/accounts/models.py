from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=100, unique=True, default="")
    password = models.CharField(max_length=300)

    class Meta:
        db_table = "users"
