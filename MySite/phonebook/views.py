from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, UpdateView, DeleteView, CreateView, FormView, View)
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import Editform
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


class Main_list(ListView):

    model = Otdelenia#.objects.order_by('FIO')
    template_name = 'body.html'
    context_object_name = 'data'
    page = 25
    paginate_by = page

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        return ordering


"""class Edit(UpdateView):

    #LoginRequiredMixin
    #form_class = CreateForm
    model = Otdelenia
    template_name = 'edit.html'
    context_object_name = 'data'
    success_url = reverse_lazy('main')
    form_class = Editform"""


class Search(ListView):

    model = Otdelenia
    template_name = 'body.html'
    context_object_name = 'data'

    def get(self, request):
        name = self.request.GET.get("full_name")
        number = self.request.GET.get("phone_number")
        dolshnost = self.request.GET.get("dolshnost")
        otdelenie = self.request.GET.get("otdelenie")
        self.model = Otdelenia.objects.filter(FIO__icontains=name, Telephon__icontains=number, Dolshnost__icontains=dolshnost, Otdelenie__icontains=otdelenie)
        return render(request, 'body.html', {'data': self.model})


class Create(CreateView):

    model = Otdelenia
    context_object_name = 'data'
    template_name = 'edit.html'
    fields = '__all__' #["full_name", "phone_number", "phone_type", "comment"]
    success_url = reverse_lazy('')


class Delete(DeleteView):  #LoginRequiredMixin,

    model = Otdelenia
    success_url = "/"
    #success_url = reverse_lazy('/')
    template_name = 'delete.html'
    context_object_name = 'data'


def edit(request, pk):
    person = get_object_or_404(Otdelenia, pk=pk)
    if request.method == "POST":
        form = Editform(request.POST, instance=person)
        if form.is_valid():
            form.save()
            """return HttpResponse(status=204, headers={
                'HX-Trigger': json.dumps({"custom_event": True, "showMessage": f"{Otdelenia.FIO} added."})})"""
            return HttpResponse(status=204, headers={'HX-Trigger': 'movieListChanged'})
    else:
        form = Editform(instance=person)
    return render(request, 'edit.html', {
        'form': form,
    })

