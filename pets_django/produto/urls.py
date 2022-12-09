from django.urls import path, include

from produto import views

urlpatterns = [
    path('latest-produtos/', views.LatestProdutosList.as_view()),
    path('produtos/pesquisa/', views.pesquisa),
    path('produtos/<slug:categoria_filtro>/<slug:produto_filtro>/', views.ProdutoDetalhe.as_view()),
    path('produtos/<slug:categoria_filtro>/', views.CategoriaDetalhe.as_view()),
]