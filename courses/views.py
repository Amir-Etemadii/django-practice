from django.shortcuts import render, redirect
from .models import Course

def course_list(request):
    courses= Course.objects.all()
    return render(request, 'courses/courses_list.html', context={'courses':courses})

def course_details(request, course_id):
    course= Course.objects.get(id=course_id)
    if course.status:
        course.status = False
    else:
        course.status = True

    course.view+= 1
    course.save()
    return render(request, 'courses/courses_details.html', context={'course':course})

def course_add(request):
    if request.method == 'POST':
        title= request.POST.get('title')
        body= request.POST.get('body')
        teacher= request.POST.get('teacher')
        photo= request.FILES.get('photo')

        Course.objects.create(title=title, body=body, teacher_nama=teacher, photo=photo)
        return redirect('courses:list')
    return render(request, 'courses/course_add_form.html', {})