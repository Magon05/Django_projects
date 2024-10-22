from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (ListView, UpdateView, DeleteView, CreateView, FormView, View)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .tables import PersonTable
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView
from .filter import PersonFilter


class Login(LoginView):

    form_class = LoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('main')


class Register(FormView):

    form_class = UserRegister
    success_url = reverse_lazy('main')
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(Register, self).form_valid(form)


class Create(LoginRequiredMixin, CreateView):

    model = Person
    template_name = 'edit.html'
    fields = '__all__' #["full_name", "phone_number", "phone_type", "comment"]
    success_url = "main"


class Edit(LoginRequiredMixin, UpdateView):

    #form_class = CreateForm
    model = Person
    fields = "__all__"
    template_name = 'edit.html'
    context_object_name = 'persons'
    #success_url = reverse_lazy('main')

    """def post(self, request, pk):
        self.model = Person.objects.get(id=pk)
        self.model.full_name = request.POST.get("full_name")
        self.model.phone_number = request.POST.get("phone_number")
        self.model.persons.phone_type = request.POST.get("phone_type")
        self.model.persons.comment = request.POST.get("comment")
        self.model.persons.save()
        return HttpResponse(headers={'HX-Trigger': json.dumps({"movieListChanged": None})})"""


class Delete(LoginRequiredMixin, DeleteView):

    model = Person
    #success_url = "/"
    success_url = reverse_lazy('main')
    template_name = 'delete.html'


class Logout(LogoutView):

    next_page = "main"  # settings.LOGOUT_REDIRECT_URL


class Main(SingleTableMixin, FilterView):

    table_class = PersonTable
    model = Person
    template_name = 'index.html'
    filterset_class = PersonFilter


def edit(self, request, id):

    if request.method == "POST":
        persons = Person.objects.get(id=id)
        persons.full_name = request.POST.get("full_name")
        persons.phone_number = request.POST.get("phone_number")
        persons.phone_type = request.POST.get("phone_type")
        persons.comment = request.POST.get("comment")
        persons.save()
        return HttpResponse(headers={'HX-Trigger': 'movieListChanged'})
    elif request.method == "GET":
        person = Person.objects.get(id=id)
        return render(request, "edit_old.html", {"person": person})


