from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('apply',views.apply,name='apply'),
    path('<id>',views.view_detail,name='view_detail')
]