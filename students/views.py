
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    total_students = Student.objects.count()

    recent_students = Student.objects.order_by(
        '-date_registered'
    )[:5]

    context = {
        'total_students': total_students,
        'recent_students': recent_students,
    }

    return render(request, 'dashboard.html', context)

@login_required
def add_student(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = StudentForm()

    context = {
        'form': form
    }

    return render(request, 'add_student.html', context)

@login_required
def student_list(request):
    search_query = request.GET.get('search', '')
    
    students = Student.objects.all().order_by('-date_registered')
    
    if search_query:
        students = students.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(matric_number__icontains=search_query) |
            Q(department__icontains=search_query)
        )

    
    context = {
        'students': students,
        'search_query': search_query,
        'total_students': students.count()
    }
    
    return render(request, 'student_list.html', context)

@login_required
def student_detail(request, student_id):
    
    student = get_object_or_404(Student, id=student_id)
    
    context = {
        'student': student
    }
    
    return render(request, 'student_detail.html', context)


@login_required
def edit_student(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:

        form = StudentForm(instance=student)

    context = {
        'form': form,
        'student': student
    }

    return render(request, 'edit_student.html', context)
