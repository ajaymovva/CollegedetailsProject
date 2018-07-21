from onlineapp.models import *
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import *
from django.urls import reverse_lazy
from onlineapp.forms.colleges import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class CreateStudentView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    login_url = '/login/'
    permission_required = "onlineapp:add_student"
    permission_denied_message = "user does not have permission to change college"
    raise_exception = True
    model = Student
    form_class = AddStudent
    template_name = 'student_forms.html'

    # import ipdb
    # ipdb.set_trace()

    def get_context_data(self, **kwargs):
        context = super(CreateStudentView, self).get_context_data(**kwargs)
        test_form = AddMockData()
        context.update(
            {
                'student_form': context.get('form'),
                'test_form': test_form,
            }
        )
        return context

    def post(self, request, *args, **kwargs):

        college = get_object_or_404(College, pk=kwargs.get('id'))
        student_form = AddStudent(request.POST)
        test_form = AddMockData(request.POST)

        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.college = college
            student.save()

            if test_form.is_valid():
                score = test_form.save(commit=False)
                score.total = sum(test_form.cleaned_data.values())
                score.student = student
                score.save()

        return redirect('onlineapp:college_details', college.id)


class UpdateStudentView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    permission_required = "onlineapp:change_student"
    permission_denied_message = "user does not have permission to change college"
    raise_exception = True
    model = Student
    template_name = 'student_forms.html'
    form_class = AddStudent

    def get_context_data(self, **kwargs):
        # import ipdb
        # ipdb.set_trace()
        context = super(UpdateStudentView, self).get_context_data(**kwargs)
        student_form = context.get('student')
        test_form = AddMockData(instance=student_form.mocktestmarks)
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
        })
        return context

    def post(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs.get('pk'))
        form = AddStudent(request.POST, instance=student)
        test_form = AddMockData(request.POST, instance=student.mocktestmarks)
        test = test_form.save(False)
        test.total = sum(test_form.cleaned_data.values())
        form.save()
        test_form.save()
        return redirect("onlineapp:college_details", self.kwargs.get('college_id'))


class DeleteStudentView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    permission_required = "onlineapp:delete_student"
    permission_denied_message = "user does not have permission to change college"
    raise_exception = True
    model = Student
    success_url = reverse_lazy('onlineapp:colleges')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.delete(request, args, kwargs)
        return redirect("onlineapp:college_details", self.kwargs.get('college_id'))



