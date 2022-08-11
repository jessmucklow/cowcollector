from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cow, Toy
from .forms import FeedingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cows_index(request):
  cows = Cow.objects.all()
  return render(request, 'cows/index.html', {
    'cows': cows
  })

def cows_detail(request, cow_id):
  cow = Cow.objects.get(id=cow_id)
  id_list = cow.toys.all().values_list('id')
  toys_cow_doesnt_have = Toy.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(
    request,
    'cows/detail.html',
    {
      'cow': cow,
      'feeding_form': feeding_form,
      'toys': toys_cow_doesnt_have
    }
  )

class CowCreate(CreateView):
  model = Cow
  fields = ['name', 'breed', 'description', 'age']
class CowUpdate(UpdateView):
  model = Cow
  fields = ['breed', 'description', 'age']

class CowDelete(DeleteView):
  model = Cow
  success_url = '/cows/'

def add_feeding(request, cow_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.cow_id = cow_id
    new_feeding.save()
  return redirect('detail', cow_id=cow_id)

def assoc_toy(request, cow_id, toy_id):
  cow = Cow.objects.get(id=cow_id)
  cow.toys.add(toy_id)
  return redirect('detail', cow_id=cow_id)

def unassoc_toy(request, cow_id, toy_id):
  Cow.objects.get(id=cow_id).toys.remove(toy_id)
  return redirect('detail', cow_id=cow_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'