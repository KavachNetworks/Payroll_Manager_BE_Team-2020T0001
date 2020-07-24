from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import models, serializers
from rest_framework.response import Response
from rest_framework import status
from companyRegistrationAndLoginApplication.models import AdminUser, Companies
from .serializers import DepartmentSerializer, DesignationSerializer
from .models import Department, Designation
from django.contrib.auth.models import User
from rest_framework.views import APIView
# Create your views here.
from companyRegistrationAndLoginApplication.models import Companies
"""
class DepartmentViewset(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.method == "POST":
            department_serializers = serializers.DepartmentSerializer(data=request.data)
            if department_serializers.is_valid():
                dept_name = department_serializers.validated_data['departmentName']
                username = request.user.get_username()
                companyId = AdminUser.objects.filter(adminId=username).values('companyId')
                company_object = Companies.objects.get(companyId=companyId)
                dept_model = models.Department(departmentName=dept_name, companyId=company_object)
                dept_model.save()
                department_serializers.save()
                return Response(department_serializers.data, status=status.HTTP_201_CREATED)
            return Response(department_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
"""

class DepartmentView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self,request):
        username = request.user.username
        companyId = AdminUser.objects.filter(adminId=username).values('companyId')
        dept = Department.objects.filter(companyId__in=companyId)
        serializer = DepartmentSerializer(dept ,many=True)
        return Response(serializer.data)

    def post(self, request):
                data = request.data
                username = request.user.username
                companyId = AdminUser.objects.filter(adminId=username).values('companyId')
                a = Companies.objects.get(companyId__in=companyId)
                serializer = DepartmentSerializer(data=data)
                if serializer.is_valid():
                    departmentName = serializer.validated_data['departmentName']
                    dep = Department.objects.filter(departmentName=departmentName,companyId=a)
                    if dep:
                        return Response("Department Exist")
                    else:
                        serializer.save(departmentName=departmentName,companyId=a)
                        return Response(serializer.data , status=201)
                return Response("message:sorry",status=400)

                
class DepartmentdetailView(APIView):
    def get_object(self,id):
       
        return Department.objects.get(departmentId=id)   

    def get(self,request,id=None):
        departmentId=id
        instance = self.get_object(departmentId)
        serializer = DepartmentSerializer(instance)
        return Response(serializer.data)

    def put(self,request,id=None):
                departmentId=id
                data = request.data
                username = request.user.username
                companyId = AdminUser.objects.filter(adminId=username).values('companyId')
                a = Companies.objects.get(companyId__in=companyId)
                instance = self.get_object(departmentId)
                serializer = DepartmentSerializer(instance,data=data)
                if serializer.is_valid():
                    departmentName = serializer.validated_data['departmentName']
                    dep = Department.objects.filter(departmentName=departmentName,companyId=a)
                    if dep:
                        return Response("Department Exist")
                    else:
                        serializer.save()
                        return Response(serializer.data , status=201)
                return Response(status=400)


# class DesigantionView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         des = Designation.objects.all()
#         serializer = DesignationSerializer(des, many=True)
#         return Response(serializer.data)


