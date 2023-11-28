from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import Employee

@api_view(['GET','POST','PUT','DELETE'])
def Employee_list(request):
    
    if request.method == 'GET':
        id = request.GET.get('id')
        if id is not None:
            emp = Employee.objects.get(id=id)
            emp_serializer = EmployeeSerializer(emp)
            return Response(emp_serializer.data)
        
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
       
       serialize = EmployeeSerializer(data=request.data)
       if serialize.is_valid():
           serialize.save()
           return Response(serialize.data)
       return Response(serialize.errors)
   
    elif request.method == 'PUT':
        id = request.GET.get('id')
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee, data = request.data, partial = True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
    elif request.method == 'DELETE':    
        id = request.GET.get('id')
        employee = Employee.objects.get(id=id)
        employee.delete()
        return Response({'Message':'Employee object deleted'})