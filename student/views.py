from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import Student,Parent


class StudentListView(ListView):
    model = Student
    paginate_by = 3


class StudentCreateView(CreateView):
    model = Student
    fields = ['family_name','given_name','family_name_huri','given_name_huri','birth','gender','address','career',
              'firstyear_class','firstyear_number','secondyear_class','secondyear_number','thirdyear_class','thirdyear_number']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'


class StudentDetailView(DetailView):
    model = Student


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['family_name','given_name','family_name_huri','given_name_huri','birth','gender','address','career',
              'firstyear_class','firstyear_number','secondyear_class','secondyear_number','thirdyear_class','thirdyear_number']
    template_name_suffix = "_update"


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('list')
