from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    path('operations/',views.operations,name='operations')
    #path('operations/',views.operations,name='subtraction'),
    #path('operations/',views.operations,name='multiplication'),
    #path('operations',views.operations,name='division')
]