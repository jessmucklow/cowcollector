from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cows/', views.cows_index, name='index'),
  path('cows/<int:cow_id>/', views.cows_detail, name='detail'),
  path('cows/create/', views.CowCreate.as_view(), name='cows_create'),
  path('cows/<int:pk>/update/', views.CowUpdate.as_view(), name='cows_update'),
  path('cows/<int:pk>/delete/', views.CowDelete.as_view(), name='cows_delete'),
  path('cows/<int:cow_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('cows/<int:cow_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('cows/<int:cow_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]
