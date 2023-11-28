from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    emp_id = models.CharField(max_length=10,blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
