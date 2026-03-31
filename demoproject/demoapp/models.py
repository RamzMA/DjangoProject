from django.db import models

# Create your models here.

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name", null=True)

    def __str__(self):
        return self.name + " : " + str(self.category_id)
    
class ApplicationForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=251)
    drinks = (('coffee', 'coffee'),('tea', 'tea'),('chantea', 'chantea'))
    drinksChoice = models.CharField(max_length=20, choices=drinks)