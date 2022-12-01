from django.urls import path
from .import views

urlpatterns =[
    path('', views.home, name='home'),
    path('hotel/', views.hotel),
    path('data/', views.data, name='data'),
    path('data/add/', views.add, name='add'),
    path('data/add/addrecord/', views.addrecord, name='addrecord'),
    path('data/delete/<int:id>/', views.delete, name='delete'),
    path('data/update/<int:id>/', views.update, name='update'),
    path('data/update/<int:id>/updaterecord/', views.updaterecord, name='updaterecord'),
]