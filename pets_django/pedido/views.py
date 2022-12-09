from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pedido, PedidoItem
from .serializers import PedidoSerializer, MeuPedidoSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def confira(request):
    serializer = PedidoSerializer(data=request.data, context={'request': request})
    print(request.data)
    if serializer.is_valid():
        total_pago = sum(item.get('quantidade') * item.get('produto').preco for item in serializer.validated_data['items'])

        try:

            serializer.save(user=request.user, total_pago=total_pago)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            raise(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    print(serializer.erro)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PedidoLista(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        pedido = Pedido.objects.filter(user=request.user)
        serializer = MeuPedidoSerializer(pedido, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PedidoSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)