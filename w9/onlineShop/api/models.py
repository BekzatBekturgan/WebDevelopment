from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(default='')
    count = models.IntegerField(default=0)
    category_id = models.IntegerField(default=0)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category_id': self.category_id

        }


class Category(models.Model):
    name = models.CharField(max_length=100)

    def to_json_c(self):
        return {
            'id': self.id,
            'name': self.name,
        }
