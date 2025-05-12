from django.shortcuts import render, get_list_or_404, redirect
#from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

# Create your views here.

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