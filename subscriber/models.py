from django.db import models

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=200)
    address_line_one = models.CharField(max_length=200)
    address_line_two = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()
    source = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
