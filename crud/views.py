from django.http import HttpResponse
from django.shortcuts import render
from crud.models import Student
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def index(request):
  students = Student.objects.all()
  return render(request, "crud/index.html", context={'students': students})

def addStd(request):
  if request.method == 'POST':
    if request.POST['name'] and request.POST["email"] and request.POST["phone"]:
      student = Student(name=request.POST['name'], email=request.POST["email"], phone=request.POST["phone"])
      student.save()
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def editStd(request, id):
  if id:
    student = Student.objects.get(id=id)
    return render(request, "crud/editstd.html", context={'student': student})

def updateStd(request):
  if request.method == 'POST':
    if request.POST['name'] and request.POST["email"] and request.POST["phone"]:
      Student.objects.filter(id=request.POST['id']).update(name=request.POST['name']
                                                           ,email=request.POST['email']
                                                           ,phone=request.POST['phone'])
      return redirect("index")

def deleteStd(request, id):
  Student.objects.filter(id=id).delete()
  return redirect("index")

