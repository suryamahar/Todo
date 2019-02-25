from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('delete/<list_id>', views.delete, name="delete"),
    path('Uncross/<list_id>', views.uncross, name="Uncross"),
    path('cross_off/<list_id>', views.cross_off, name="cross_off"),

]
