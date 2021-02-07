from django.db.models import CharField, Model 
from django.db import models
from django_mysql.models import ListCharField

class Person(models.Model):
    email 					= models.EmailField(max_length=60)
    first_name 				= models.CharField(max_length=30)
    last_name               = models.CharField(max_length=30)
    favorites = ListCharField(
        base_field=CharField(max_length=10),
        size=10,
        max_length=(10 * 11)  # 6 * 10 character nominals, plus commas
    )
  