from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegisterForm

#login view 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
#logout view 
from django.contrib.auth import logout 

#login protection
# from django.contrib.auth.decorators import login_required
# # Create your views here.

# def home(request):
#     #return render(request, 'home.html')
#     # content = {
#     #     'head' : "Django Template",
#     #     'message' : "This is generated with Django template"
#     # }
#     if request.method == 'POST': 
#         form = NameForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['your_name']
#             return render(request, 'myapp/home.html', {
#                 'form' : form,
#                 'head' : "Django Template",
#                 'message' : "This is generated with Django template",
#                 'name' : name
#             })
#     else : 
#         form = NameForm()
#     return render(request, 'myapp/home.html', {
#         'form': form,
#         'head': "Django Template",
#         'message': "This is generated with Django template"
#     })
#     #return render(request, 'myapp/home.html', content)

    
def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/success.html')
    else:
        form = StudentForm()

    return render(request, 'myapp/student_form.html', {'form' : form})       
# @login_required(login_url='login')
def student_list_view(request):
    students = Student.objects.all() # Fetch all student records 
    return render(request, 'myapp/student_list.html', {'students': students})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id) # Fetches Existing student

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'myapp/edit_student.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'myapp/delete_confirm.html', {'student': student})

# authentication system
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_list')
    else:
        form = RegisterForm()

    return render(request, 'myapp/register.html', {'form': form})

#Login  View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('student_list')

    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})       

# Logout view 
def logout_view(request):
    logout(request) 
    return redirect('login')