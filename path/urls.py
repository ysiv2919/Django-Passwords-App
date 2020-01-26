from django.urls import path
from . import views

app_name = 'path'

urlpatterns = [
    path('', views.index, name='index'),
    path('new-password', views.new_password, name='new-password'),
    path('delete-password/<int:password>', views.delete_password, name='delete-password')
]