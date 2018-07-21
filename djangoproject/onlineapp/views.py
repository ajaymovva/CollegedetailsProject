from django.shortcuts import render

import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response
from onlineapp.models import *


# Create your views here.
def current_datetime(request):
    object = College.objects.values('name', 'acronym')
    return render(request, 'collegedata.html', {'object': object})


def studentinfo(request):
    object = Student.objects.values('college__acronym', 'name', 'email', 'db_folder')
    return render(request, 'student_acronym.html', {'object': object})


def dynamicrender(request, id):
    object = Student.objects.filter(id=id).values('name', 'email')
    return render(request, 'dynamic.html', {'object': object})


def studentinfoonclick(request):
    object = Student.objects.values('name', 'email', 'college__acronym', 'mocktestmarks__total',
                                    'dropped_out').order_by('college__acronym')
    return render(request, 'student_onclick.html', {'object': object})


def collegebyorder(request, acronym):
    object = MockTestMarks.objects.filter(student__college__acronym=acronym).values('student__name', 'student__email',
                                                                                    'total').order_by('total')
    return render(request, 'sortcollege.html', {'object': object})


def login(request):
    request.session.setdefault('count', 0)
    countvalue = request.session['count'] + 1
    request.session['count'] = countvalue
    return HttpResponse(request.session['count'])
