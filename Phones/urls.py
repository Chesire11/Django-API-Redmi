from django.urls import path
from . import views
from .views import redmi_with_variants

urlpatterns = [
    path('', views.index, name='index'),
    path('redmi/', views.redmi_list, name='redmi_list'), 
    path('redmi/<int:redmi_id>/', views.redmi_detail, name='redmi_detail'),
    path('api/redmi/', redmi_with_variants, name='redmi-with-variants'),
]