from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=100)
    company_name = serializers.CharField(max_length=150)
    emp_id = serializers.CharField(max_length=10)
    
    def create(self, data):
        return Employee.objects.create(**data)
    
    def update(self, instance, data):
        instance.name = data.get('name' , instance.name)
        instance.company_name = data.get('company_name', instance.company_name)
        instance.emp_id = data.get('emp_id', instance.emp_id)
        
        instance.save()
        return instance