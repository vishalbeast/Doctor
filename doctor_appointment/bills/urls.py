from django.urls import path
from . import views
from .views import *
from bills.views import *
app_name = 'bill'

urlpatterns = [
    path('billIndex/',views.index,name='index'),
    path('bill/',views.cal_amount,name='cal_amount'),
    path('test/billIndex',views.test_iterations,name='test_iterations')
]
