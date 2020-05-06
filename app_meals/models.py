# meals/models.py
from django.db import models
from django.utils.text import slugify

class Meals(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    preperation_time =models.IntegerField()
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blank=True, null=True)

    # add name automaticall to slug if the slug field is empty
    def save(self , *args , **kwargs):
        # if the slug field is empty, but name field is NOT empty
        if not self.slug and self.name :
            # then add the name to slug field
            self.slug = slugify(self.name)
            # then save the name to slug
        super(Meals , self).save(*args , **kwargs)

    # Convert table's name from Mealss to Meals
    # Note: by default django will add 's' to Model name ('Meals' to 'Mealss' ) automatically
    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    # Convert object of a name to a string
    def __str__(self):
        return self.name
