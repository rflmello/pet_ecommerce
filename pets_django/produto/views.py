from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer

class LatestProdutosList(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        produtos = Produto.objects.all()[0:4]
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

class ProdutoDetalhe(APIView):
    authentication_classes = []
    permission_classes = []

    def get_object(self, categoria_filtro, produto_filtro):
        try:
            return Produto.objects.filter(categoria__filtro=categoria_filtro).get(filtro=produto_filtro)
        except Produto.DoesNotExist:
            raise Http404
    
    def get(self, request, categoria_filtro, produto_filtro, format=None):
        produto = self.get_object(categoria_filtro, produto_filtro)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

class CategoriaDetalhe(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get_object(self, categoria_filtro):
        try:
            return Categoria.objects.get(filtro=categoria_filtro)
        except Categoria.DoesNotExist:
            raise Http404
    
    def get(self, request, categoria_filtro, format=None):
        categoria = self.get_object(categoria_filtro)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

@api_view(['POST'])
def pesquisa(request):
    query = request.data.get('query', '')

    if query:
        produtos = Produto.objects.filter(Q(nome__icontains=query) | Q(descricao__icontains=query))
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    else:
        return Response({"produtos": []})
