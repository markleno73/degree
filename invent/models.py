from django.db import models
from django.http import HttpResponse

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=300)
    desc = models.
    date_added = models.DateTimeField('date added')


class ItemTag(models.Model):
    name = models.CharField(max_length=300)


class ItemToTagCor(models.Model):
    name = models.ForeignKey(Item, on_delete=models.CASCADE)


class ItemLocation(models.Model):
    closet = models.ForeignKey(locationapp)


# inventory items have a location
# inventory items have a type
# inventory items have a manufacturer
# inventory items have a model
# inventory items have a serial number
# inventory items have history ( like location, shipping, purchase, manufacture, support and warranty )
# inventory items have item_properties (multiple properties, maybe even property sets)

# item_properties have a type
# item_properties have a name
# item_properties have a value

# inventory location is a foreign key to locations
# locations are owned by a company
# locations have contacts
# locations have procedures ( access procedures, etc. )
# locations have addresses
# locations have a history
# locations have types

# inventory types have a name
# inventory types have a description
# inventory types have relationships to other inventory types.

# inventory manufacturers is a foreign key to companies
# manufacturers have a foreign key to locations
# manufacturers history ( like
# manufacturers have notes
# inventory model is a foreign key to models

# inventory

# important dates have a type
# important dates have a date
# important dates have a name

