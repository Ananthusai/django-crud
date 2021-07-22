from django.shortcuts import render, redirect  
from student.forms import StudentForm 
from student.models import Student 
  
def stu(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                return 'your input is incomplete or invalid' 
    else:  
        form = StudentForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    students = Student.objects.all()  
    return render(request,"show.html",{'students':students})  

def edit(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'edit.html', {'student':student})

def update(request, id):  
    student = Student.objects.get(id=id)  
    student_form = StudentForm(request.POST or None, instance = student)  
    if student_form.is_valid():  
        student_form.save()  
        return redirect("/show") 
    else:   
        return render(request, 'edit.html', {'student': student})  

def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/show")  
