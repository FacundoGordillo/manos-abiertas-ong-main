from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Noticia, Comentario
from sistema.forms import ComentarioForm
from django.urls import reverse_lazy, reverse
# Create your views here.

class NoticiaListView(ListView):
    model = Noticia
    template_name = "noticias/ListadoNoticias.html"

class NoticiaDetalleView(DetailView):
    model = Noticia
    template_name = "noticias/detalleNoticia.html"
    
class AddComentarioView(CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'noticias/agregar_comentarios.html'
    #fields = '__all__'
    success_url = reverse_lazy('home')