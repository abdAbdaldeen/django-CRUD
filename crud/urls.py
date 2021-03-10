from django.urls import path
from .views import index,addStd,editStd,updateStd,deleteStd

urlpatterns = [
    path('', index, name="index"),
    path('addStd', addStd , name="addStd"),
    path('editStd/<id>', editStd , name="editStd"),
    path('updateStd', updateStd , name="updateStd"),
    path('deleteStd/<id>', deleteStd , name="deleteStd"),
]
