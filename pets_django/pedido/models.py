from django.contrib.auth.models import User
from django.db import models

from produto.models import Produto

class Pedido(models.Model):
    user = models.ForeignKey(User, related_name='pedidos', on_delete=models.CASCADE)
    primeiro_nome = models.CharField(max_length=100)
    segundo_nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField(max_length=100)       
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    total_pago = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    # stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ['-data_criacao',]
    
    def __str__(self):
        return self.primeiro_nome

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='items', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id