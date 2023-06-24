from django.urls import path
from .views import *

urlpatterns=[
    path('',showPerson,name='showPerson'),
    path('add/',Addperson,name='add'),
    path('edit/',edit_customer,name='edit'),
    path('Delete_data/',Delete_data,name='Delete_data'),
    path('deltise/',deltaisPer,name='deltise')
    
]