from django.db import models

#Iremos importar um model padrão do  app auth já criado pelo Django pra pegarmos informações sobre o autor do post:

from django.contrib.auth.models import User

from django.urls import reverse

from PIL import Image


class Post(models.Model):
    
    title = models.CharField(max_length=255)
    
    #AQUI ESTOU CRIANDO O CAMPO QUE IRÁ NA URL PARA DIRECIONAR PARA UM POST ESPECÍFICO 
    slug = models.SlugField(max_length=255, unique=True)
                        #on_delete .CASCADE está definindo que, caso o autor seja deletado, o post também será deletado.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    body = models.TextField()
    
            #Aqui estou mandando ele pegar automaticamente a hora do sistema e atribuir à variável que irá guardar a data e hora de criação do post
    created = models.DateTimeField(auto_now_add=True)
                    
                    #Note que esse não tem o add igual acima
    updated = models.DateTimeField(auto_now=True)

    photo = models.ImageField(upload_to='static')
    

    #Essa meta está fazendo os posts serem exibidos do mais recente para o mais antigo
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})



