from django.views.generic import DetailView, ListView


from .models import Post


#Vamos começar a criar as classes aqui

class PostListView(ListView):
    model = Post

class PostDetalView(DetailView):
    model = Post
