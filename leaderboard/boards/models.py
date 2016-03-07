from django.db import models


# Create your models here.
class Item(models.Model):
    """
    Description: Can be a name of a person, brand, object, etc.
    """
    item_text = models.CharField(max_length=255)
    score = models.IntField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
