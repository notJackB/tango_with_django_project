from django.db import models

#category class with name as primary key
#pass in the model from models to allow for database creation
class Category(models.Model):
    name= models.CharField(max_length=128, unique=True)
    views= models.IntegerField(default=0)
    likes= models.IntegerField(default=0)

    class Meta:
        verbose_name_plural= 'Categories'

    #method to return the object's name
    def __str__(self):
        return self.name

#page class that has the one to many realtionship to category
class Page(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    #SQL to do make sure that if PK is deleted from category,
    #remove associated FKs here
    title= models.CharField(max_length=128)
    url= models.URLField()
    views= models.IntegerField(default=0)

    def __str__(self):
        return self.title
