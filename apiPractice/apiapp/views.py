from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import EmployeeModel
from .serializers import EmployeeSer
from rest_framework.response import Response

# Create your views here.
class data(APIView):
    def get(self,r,pk,*args,**kwargs):
        qs = EmployeeModel.objects.get(employee_id=pk)
        serObj = EmployeeSer(qs)
        return Response(serObj.data)
