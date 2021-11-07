from django.urls import path

from gasparconsultoria.views import *

urlpatterns = [
    path('', index, name='index'),
    path('sobre-nos/', sobre, name='sobre'),
    path('servicos/laudos/', laudos, name='laudos'),
    path('servicos/pericias/', pericias, name='pericias'),
    path('servicos/treinamentos/', treinamentos, name='treinamentos'),
    path('servicos/assessoria/', assessoria, name='assessoria'),
    path('contato/', contato, name='contato'),
    path('clientes/', clientes, name='clientes'),
]