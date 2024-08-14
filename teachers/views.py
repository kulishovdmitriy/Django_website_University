from django.shortcuts import render, reverse, get_object_or_404
from django.http.response import HttpResponseRedirect

from teachers.models import Teacher
from teachers.forms import TeacherCreateForms, TeacherEditForms


# Create your views here.


def get_teachers(request):
    teachers = Teacher.objects.all()

    params = [
        "first_name",
        "last_name",
        "birthdate",
        "subject",
        "years_of_experience",

    ]
    for param in params:
        value = request.GET.get(param)
        if value:
            teachers = teachers.filter(**{param: value})

    return render(
        request,
        "teachers_list.html",
        {"teachers": teachers},
    )


def create_teacher(request):

    if request.method == "GET":
        form = TeacherCreateForms()

    if request.method == "POST":
        form = TeacherCreateForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("teachers:list"))

    return render(
        request,
        "teacher_create.html",
        {"form": form}
    )


def edit_teacher(request, uuid):

    teacher = get_object_or_404(Teacher, uuid=uuid)

    if request.method == "GET":
        form = TeacherEditForms(instance=teacher)

    elif request.method == "POST":
        form = TeacherEditForms(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("teachers:list"))

    return render(
        request,
        "teacher_edit.html",
        {
            "form": form,
            "teacher": teacher,
            "students": teacher.students.all(),
        }
    )


def delete_teacher(request, uuid):

    teacher = get_object_or_404(Teacher, uuid=uuid)

    teacher.delete()

    return HttpResponseRedirect(reverse("teachers:list"))
