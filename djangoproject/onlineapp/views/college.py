# from .college import *
# from .student import *
# from .auth import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from onlineapp.models import *
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import *
from django.urls import reverse_lazy
from onlineapp.forms.colleges import *


class CollegeView(View):
    def get(self, request, *args, **kwargs):
        colleges = College.objects.all()

        return render(request, template_name='firstclass.html', context={'object': colleges})
        pass


class CollegeListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = College
    context_object_name = 'object'
    template_name = 'collegedisplaybylink.html'

    def get_context_data(self, **kwargs):
        context = super(CollegeListView, self).get_context_data(**kwargs)
        # import ipdb
        # ipdb.set_trace()
        context['data'] = self.model.objects.all()
        context.update({'user_permissions': self.request.user.get_all_permissions()})
        return context


class CollegeDetailsView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = College
    template_name = 'detailviewcollege.html'

    def get_object(self, queryset=None):
        return get_object_or_404(College, **self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(CollegeDetailsView, self).get_context_data(**kwargs)
        college = context.get('college')
        students = list(
            college.student_set.values('name', 'mocktestmarks__total', 'email', 'id').order_by("-mocktestmarks__total"))
        context.update({
            'object': students,
            'user_permissions': self.request.user.get_all_permissions()
        })
        return context


class CreateCollegeView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = '/login/'
    permission_required = "onlineapp:add_college"
    permission_denied_message = "user does not have permission to change college"
    raise_exception = True
    model = College
    form_class = AddCollege
    template_name = 'college_forms.html'
    success_url = reverse_lazy('onlineapp:colleges')


class EditCollegeView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = '/login/'
    permission_required = "onlineapp:change_college"
    permission_denied_message = "user does not have permission to change college"
    # import ipdb
    # ipdb.set_trace()
    raise_exception = True
    model = College
    form_class = AddCollege
    template_name = 'college_forms.html'
    success_url = reverse_lazy('onlineapp:colleges')


class DeleteCollegeView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    permission_required = "onlineapp:delete_college"
    permission_denied_message = "user does not have permission to delete college"
    raise_exception = True
    model = College
    form_class = AddCollege
    success_url = reverse_lazy('onlineapp:colleges')

    def get(self, request, *args, **kwargs):
        return self.post(request, args, kwargs)


# class CollegeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = College
#         fields = ('name','location','acronym','contact')
