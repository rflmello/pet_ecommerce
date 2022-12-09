from rest_framework import serializers

from .models import Categoria, Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            "id",
            "nome",
            "get_url",
            "descricao",
            "preco",
            "get_imagem",
            "get_imagem_pequena"
        )

class CategoriaSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True)

    class Meta:
        model = Categoria
        fields = (
            "id",
            "nome",
            "get_url",
            "produtos",
        )