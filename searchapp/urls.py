from django.urls import path
from . import views

app_name = 'searchapp'

urlpatterns = [

    path('',views.Search_result,name='Search_result'),

]
