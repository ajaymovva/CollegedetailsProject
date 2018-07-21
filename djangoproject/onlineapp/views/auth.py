from onlineapp.forms.auth import *
from django.views import View
from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import base64
from django.contrib.auth import authenticate
from django.http import JsonResponse


class Signupclass(View):
    def get(self, request, *args, **kwargs):
        template_name = "signupform.html"
        form = Signupform()
        context = {'form': form, 'title': 'signup'}
        return render(request, template_name, context)

    def post(self, request):
        form = Signupform(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect("onlineapp:colleges")
            else:
                return redirect("errorpage.html")
        else:
            return redirect("onlineapp:signup")


def logout_user(request):
    logout(request)
    return redirect('onlineapp:login')


class LoginClass(View):
    def get(self, request, *args, **kwargs):
        template_name = "loginform.html"
        form = Loginform()
        context = {'form': form, 'title': 'login'}
        return render(request, template_name, context)

    def post(self, request):
        form = Loginform(request.POST)
        if form.is_valid():
            # user = User.objects.create_user(**form.cleaned_data)
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect("onlineapp:colleges")
            else:
                return redirect("errorpage.html")
        else:
            return redirect("onlineapp:login")


def basic_authentication(data_function):
    def wrapper(request, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    username, password = base64.b64decode(auth[1]).split(b':', 1)
                    username = username.decode('utf-8')
                    password = password.decode('utf-8')
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        return data_function(request)

                        # otherwise ask for authentification
        return JsonResponse({'WWW-Authenticate': 'Basic realm="restricted area"'}, status=401)

    return wrapper
