from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    rating = models.IntegerField()
    prep_time = models.TimeField('preparation time')
    cook_time = models.TimeField('cooking time')
    diners = models.IntegerField()
    difficulty = models.IntegerField()
    # TODO: add photo, author

