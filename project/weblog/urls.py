from django.urls import path
from . import views

urlpatterns=[
    path('weblog/', views.weblog, name='weblog'),
    path('coba2/', views.coba2, name='coba2'),
]