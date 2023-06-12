from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, blank = False)
    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = 'images',null=True, blank = True)
    slug = models.SlugField(max_length=100, unique=True, default=0.0)

    def __str__(self):
        return "{id}-{title}".format(id=self.id, title=self.name)
    
    def get_absolute_url(self):
        return reverse('cars:vehicle_list_by_category', args=[self.slug])
    
class Vehicle(models.Model):
    model = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    km = models.PositiveIntegerField()
    engine = models.FloatField()
    transmission = models.CharField(max_length=10)
    fuel = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name='vehicle', null=True, blank = True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'images', null=True, blank = True)
    slug = models.SlugField(max_length=100, unique=True, default=0.0)

    def __str__(self):
        return "{model}-{category}".format(model=self.model, category = self.category)

    def get_absolute_url(self):
        return reverse('cars:vehicle_details', args=[self.id, self.slug])