from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    filtro = models.SlugField()

    class Meta:
        ordering = ('nome',)
    
    def __str__(self):
        return self.nome
    
    def get_url(self):
        return f'/{self.filtro}/'

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    filtro = models.SlugField()
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='uploads/', blank=True, null=True)
    imagem_pequena = models.ImageField(upload_to='uploads/', blank=True, null=True)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data_adicionado',)
    
    def __str__(self):
        return self.nome
    
    def get_url(self):
        return f'/{self.categoria.filtro}/{self.filtro}/'
    
    def get_imagem(self):
        if self.imagem:
            return 'http://127.0.0.1:8000' + self.imagem.url
        return ''
    
    def get_imagem_pequena(self):
        if self.imagem_pequena:
            return 'http://127.0.0.1:8000' + self.imagem_pequena.url
        else:
            if self.imagem:
                self.imagem_pequena = self.make_imagem_pequena(self.imagem)
                self.save()

                return 'http://127.0.0.1:8000' + self.imagem_pequena.url
            else:
                return ''
    
    def make_imagem_pequena(self, imagem, size=(300, 200)):
        img = Image.open(imagem)
        img.convert('RGB')
        img.imagem_pequena(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        imagem_pequena = File(thumb_io, nome=imagem.nome)

        return imagem_pequena