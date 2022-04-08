from django.urls import path
from .views import VRegistro, cerrar_sesion, Vlogin


urlpatterns = [
    path('', VRegistro.as_view(), name='autenticacion'),
    path('cerrar', cerrar_sesion, name='cerrar_sesion'),
    path('logear',Vlogin.as_view(), name='logear')
]