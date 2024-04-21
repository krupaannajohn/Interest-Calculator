# Create your models here.
# we'll create 5 fields for the strorage in our dbs. we will store principal amount, rate of interest, time period, total SI value and the timestamp of storage
# this will contain all the table data and structure in sql

from django.db import models

class Calculation(models.Model):
    principal = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.IntegerField()
    result = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

#once we click on make migrations, itll automatically create a table with these fields in the database
# whenever we make changes to the model, we must always make migrations and migrate else it will not reflect