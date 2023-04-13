from django.urls import path
from . import views
urlpatterns=[
    path('',views.stock_picker, name="stockpicker"),
    path('stocktracker/',views.stock_tracker,name='stocktracker'),
]