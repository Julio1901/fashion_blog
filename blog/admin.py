from django.contrib import admin

# Register your models here.

from .models import Post



#Opcional, para aparecer informações sobre o post na interface de admin
@admin.register(Post)

class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated')

    #Para o campo slug ser preenchido altomaticamente conforme formos escrevendo o post:
                        #Não esqueça a vírgula
    prepopulated_fields = {'slug': ('title',)}
