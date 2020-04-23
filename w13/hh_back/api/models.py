from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=300, default="")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=500, default="")
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary

        }
