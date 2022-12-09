from django.urls import path

from pedido import views

urlpatterns = [
    path('confira/', views.confira),
    path('pedidos/', views.PedidoLista.as_view()),  
]