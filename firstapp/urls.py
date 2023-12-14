from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [

    path('',views.all_Product_Category,name='all_Product_Category'),
    path('<slug:c_slug>/',views.all_Product_Category,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.Product_Details,name='Product_Details'),


]