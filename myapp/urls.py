from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delrecord, name='delete'),
    path('update/<int:id>', views.uprecord, name='update'),
    path('update/addupdate/<int:id>', views.updaterecord, name='addupdate'),
]