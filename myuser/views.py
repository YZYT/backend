from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from django.db import connection



# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    # 获取游标对象
    cursor = connection.cursor()
    # 拿到游标对象后执行sql语句
    cursor.execute("select * from users")
    # 获取所有的数据
    rows = cursor.fetchall()
    # 遍历查询到的数据
    for row in rows:
        print(row)
    return HttpResponse("Login.")
    # students = []
    # for student in User.objects.all():
    #     students.append({
    #         'name': student.name,
    #         'age': student.age
    #     })
    # return JsonResponse(students, safe=False)


