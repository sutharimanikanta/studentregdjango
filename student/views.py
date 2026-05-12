from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        rolno = request.POST.get("rolno")
        branch = request.POST.get("branch")
        student = Student(name=name, rolno=rolno, branch=branch)
        student.save()
        messages.success(request, "Student registered successfully.")
        return redirect("/students/")
    return render(request, "register.html")


def students(request):
    if request.method == "GET":
        stud = Student.objects.all()
        return render(request, "students.html", {"students": stud})
