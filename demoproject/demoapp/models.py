from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name", null=True)

    def __str__(self):
        return self.name + " : " + str(self.category_id)
    
