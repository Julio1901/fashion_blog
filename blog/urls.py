from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    #Conectando a url sem argumentos com a PostListView do views
    path('', views.PostListView.as_view(), name='list'),
    path('index.html', views.PostListView.as_view(), name='list'),
    #Conectando à um post quando passamos uma url que tem um slug como argumento
    path('<slug:slug>/', views.PostDetalView.as_view(), name='detail'),
    
#Como estamos trabalhando com views baseadas em classes, precisamos chamar esse método .as_view(), ele irá receber a requisição web

#O name é o que iremos usar para referenciar esses padrões acima

    path('author.html', views.author_page, name='author_page')

]

#Como eu tenho um app_name e tenho o name nos padrões, eu evito conflito com outros apss que poderiam, por exemplo, ter uma url com name 'list'' ou name 'detail'


