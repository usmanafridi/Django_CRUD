from django.db import models

from django.utils.timezone import now


# Name of class/model will be name of Table in database
# Field Types
# - Character (CharField)
# - Text (TextField)
# - IntegerField
# - FloatField
# - BooleanField
# - FileField or ImageField

# Common Attributes for Fields
# null = if field can be null,
# unique = if this field is unique
# blank = if this field required
# default = default value 

# Relations

# ORM = Object Relational Mapping
class Mobile(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    price = models.IntegerField()
    is_new = models.BooleanField(default=True)
    features = models.TextField()

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=60)
    reg_no = models.CharField(max_length=19)



class Booking(models.Model):
    name= models.CharField(max_length=30)
    email= models.EmailField()
    date = models.DateTimeField(default=now, editable=False)
    with_family= models.BooleanField(default=False)
    room=models.IntegerField()

