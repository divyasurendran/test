from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def student(request):
    if (request.method=="POST"):
        id=request.POST["student id"]
        name=request.POST["student name"]
        age=request.POST["student age"]
        gender=request.POST["student gender"]
        studentclass=request.POST["student class"]
        Student.objects.create(
            student_id=id,
            student_name=name,
            student_age=age,
            student_gender=gender,
            student_class=studentclass

        )
        

        print(id)
        print(name)
        print(age)
        print(gender)
        print(studentclass)

    return render(request,"students.html")

def student_view(request):
    data=list(Student.objects.all().values())
    #print(data)
    return render(request,"view.html",{"student" : data} )