from django.db import models
from django.db.models import Avg


class Img(models.Model):
    img = models.ImageField()


class Step(models.Model):
    nbStep = models.PositiveIntegerField()
    description = models.CharField(max_length=100, blank=False)
    img = models.ManyToManyField(Img, related_name="images_step")


class Tools(models.Model):
    name = models.CharField(max_length=300, blank= False)

class Keywords(models.Model):
    name = models.CharField(max_length=300, blank= False)


class Ingredients(models.Model):
    name = models.CharField(max_length=50, blank= False)
    quantity = models.CharField(max_length=50, blank= False)


class Recipe(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500)

    ingredients = models.ManyToManyField(Ingredients, verbose_name="rec_ingredients")


    time = models.PositiveIntegerField()
    steps = models.ManyToManyField(Step, verbose_name="rec_steps")
    tools = models.ManyToManyField(Tools, verbose_name="rec_tools")
    keywords = models.ManyToManyField(Keywords, verbose_name="rec_keywords")
    rating = models.PositiveIntegerField()  # en estrellas
    n_rates = models.PositiveIntegerField()

    price = models.PositiveIntegerField()

    origin = models.CharField(max_length=60)
    glucemicIndex = models.PositiveIntegerField()


    difficulty = models.CharField(max_length=30)


    #img = models.ImageField(upload_to='img')






