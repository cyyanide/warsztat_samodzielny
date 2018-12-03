from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    description = models.TextField()
    address = models.ForeignKey("Address", on_delete=models.CASCADE, null=True)

class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)
    apartment_number = models.CharField(max_length=10)

class Phone(models.Model):
    number = models.IntegerField(null=True)
    number_type = models.CharField(max_length=50)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

class Email(models.Model):
    email = models.CharField(max_length=50)
    email_type = models.CharField(max_length=50)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

class Group(models.Model):
    name = models.CharField(max_length=50)
    person = models.ManyToManyField(Person)
