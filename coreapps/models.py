from django.db import models

# Create your models here.


# Place
class Place(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(null=True, blank=True)
    # should be many to many with addresses
    address_line1 = models.CharField(max_length=200, verbose_name='Address Line 1', null=True, blank=True)
    address_line2 = models.CharField(max_length=200, verbose_name='Address Line 2', null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


# department
class Department(models.Model):
    name = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    # should be many to many with companies and Place

    def __str__(self):
        return self.name


# company
class Company(models.Model):
    name = models.CharField(max_length=200)
    # should be many to many with Place

    def __str__(self):
        return self.name


# people
class Person(models.Model):
    name = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# model number
class ModelNumber(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# things
class Thing(models.Model):
    name = models.CharField(max_length=200)
    model_num = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# kb
class KbArticle(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    Kb_text = models.CharField(max_length=10000)

    def __str__(self):
        return self.name


# notes
class Note(models.Model):
    name = models.CharField(max_length=200)
    note_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


# links
class Linker(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    urly = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
