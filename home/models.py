from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name + '-' + self.email
