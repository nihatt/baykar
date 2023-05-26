from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'


class Plane(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    image = models.TextField()
    class Meta:
        db_table = 'planes'