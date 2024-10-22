from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (View, ListView, UpdateView, DetailView, DeleteView, CreateView)
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings


class Login(LoginView):

    form_class = LoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('main')

    #ручной метод
    """def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("main/")
        else:
            return HttpResponseRedirect("/")"""


class Test(ListView):
    model = Person
    template_name = 'index.html'
    context_object_name = 'persons'


class Main(ListView):

    model = Person
    template_name = 'index.html'
    context_object_name = 'persons'
    #login_url = reverse('/main/')
    #success_url = reverse('main')

    def post(self, request):
        name = self.request.POST.get("filter")
        if Person.objects.filter(full_name__icontains=name).first() is not None:
            person = Person.objects.filter(full_name__icontains=name)
        else:
            person = Person.objects.filter(phone_number__icontains=name)
        print(person)
        return render(request, "index.html", {"persons": person})


class Create(LoginRequiredMixin, CreateView):

    model = Person
    template_name = 'create.html'
    fields = '__all__' #["full_name", "phone_number", "phone_type", "comment"]
    success_url = "/"
    #form_class = CreateForm()


class Edit(LoginRequiredMixin, UpdateView):

    model = Person
    fields = "__all__"
    template_name = 'create.html'
    context_object_name = 'persons'
    success_url = "/"
    # template_name_suffix = '_update_form'

    #ручной метод
    """def post(self, request, id):
        person = Person.objects.get(id=id)
        person.full_name = request.POST.get("full_name")
        person.phone_number = request.POST.get("phone_number")
        person.phone_type = request.POST.get("phone_type")
        person.comment = request.POST.get("comment")
        person.save()
        return HttpResponseRedirect("/")

    def get(self, request, id):
        person = Person.objects.get(id=id)
        return render(request, "edit.html", {"person": person})"""


@login_required
def Delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return HttpResponseRedirect("/")


class Logout(LogoutView):

    next_page = "main"  # settings.LOGOUT_REDIRECT_URL
    #success_url_allowed_hosts = ""
    #redirect_field_name = ""
    #template_name = 'index.html'


"""def logout_user(request):
    logout(request)
    return redirect('')"""

"""class Create_Ph_Type(View):

    def post(self, request):
        type = PhoneType()
        type.phone_type = request.POST.get("phone_type")
        type.save()
        return HttpResponseRedirect("/")"""