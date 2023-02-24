from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import For_teacherForm


def tasks(request):
    return render(request, "test_country/index.html")


def about(request):
    return render(request, "test_country/about.html")

def france(request):
    error = ''
    if request.method == 'POST':
        form = For_teacherForm(request.POST)
        mmylka = request.POST.get('France')
        if form.is_valid():
            form.save()
            return redirect('for_teacher')
        else:
            error = 'the form was wrong'

    form = For_teacherForm()
    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'test_country/France.html', context)


def brazil(request):
    return render(request, "test_country/Brazil.html")


def portugal(request):
    return render(request, "test_country/Portugal.html")


def for_teacher(request):
    subject = For_teacher.objects.order_by('-id')
    return render(request, 'test_country/for_teacher.html', {'title': 'Франция', 'subject': subject})
