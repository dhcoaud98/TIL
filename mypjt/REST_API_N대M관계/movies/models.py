from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    actors = models.ManyToManyField(Actor, related_name='actors_movie')
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()