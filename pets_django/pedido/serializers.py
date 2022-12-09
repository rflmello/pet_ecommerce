from rest_framework import serializers

from .models import Pedido, PedidoItem

from produto.serializers import ProdutoSerializer

class MeuPedidoItemSerializer(serializers.ModelSerializer):    
    produto = ProdutoSerializer()

    class Meta:
        model = PedidoItem
        fields = (
            "preco",
            "produto",
            "quantidade",
        )

class MeuPedidoSerializer(serializers.ModelSerializer):
    items = MeuPedidoItemSerializer(many=True)

    class Meta:
        model = Pedido
        fields = (
            "id",
            "primeiro_nome",
            "segundo_nome",
            "email",
            "rua",
            "cep",
            "numero",
            "complemento",
            "bairro",
            "cidade",
            "estado",
            "telefone",
            "items",
            "total_pago"
        )

class PedidoItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = PedidoItem
        fields = (
            "preco",
            "produto",
            "quantidade",
        )

class PedidoSerializer(serializers.ModelSerializer):
    items = PedidoItemSerializer(many=True)

    class Meta:
        model = Pedido
        fields = (
            "id",
            "primeiro_nome",
            "segundo_nome",
            "email",
            "rua",
            "cep",
            "numero",
            "complemento",
            "bairro",
            "cidade",
            "estado",
            "telefone",
            "items",
        )
    
    def create(self, validated_data):
        user = self.context['request'].user
        items_data = validated_data.pop('items')
        print(validated_data)
        pedido = Pedido.objects.create(**validated_data)

        for item_data in items_data:
            PedidoItem.objects.create(pedido=pedido, **item_data)
            
        return pedido