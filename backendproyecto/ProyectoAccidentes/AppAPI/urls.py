from django.urls import path
from .views import UsuarioView, TrasladosView, AmbulanciasView, GraficaView

urlpatterns=[
    path('usuarios/',UsuarioView.as_view(), name='usuarios_list'),
    path('usuarios/<int:id>',UsuarioView.as_view(), name='usuarios_process'),
    path('traslados/',TrasladosView.as_view(), name='traslados_list'),
    path('ambulance/',AmbulanciasView.as_view(), name='ambulance_list'),
    path('grafica/',GraficaView.as_view(), name='grafica')
]