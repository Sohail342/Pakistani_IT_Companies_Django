from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    rating = models.FloatField()
    location = models.CharField(max_length=255)
    
    def __str__(self):
        return self.company_name

class Client(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_clients = models.CharField(max_length=255)
    
    def __str__(self):
        return self.company_clients
