from django.db import models

class Serie(models.Model):
    HORROR = 'horror'
    COMEDY = 'comedy'
    ACTION = 'action'
    DRAMA = 'drama'
    CATEGORIES_CHOICES = (
        (HORROR, 'Horror'),
        (COMEDY, 'Comedy'),
        (ACTION, 'Action'),
        (DRAMA, 'Drama'),
    )
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)

    def __str__(self):
        return self.name

class Datos(models.Model):
    temperatura = models.DecimalField(max_digits=10, decimal_places=2)
    humedad = models.DecimalField(max_digits=10, decimal_places=2)
