from django.urls import path
from .views import category_list


app_name='categories'

urlpatterns=[
    path('categories/', category_list, name='list')
]