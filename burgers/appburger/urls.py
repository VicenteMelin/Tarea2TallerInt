from django.urls import path

from . import views

urlpatterns = [
    path('hamburguesa', views.hamburguesa_list),
    path('hamburguesa/<pk>', views.hamburguesa_detail),
    path('ingrediente', views.ingrediente_list),
    path('ingrediente/<pk>', views.ingrediente_detail, name='ingrediente-detail'),
    path('hamburguesa/<int:pkh>/ingrediente/<int:pki>', views.delete_ingrediente),

]