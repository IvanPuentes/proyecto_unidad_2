from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,DescripLib,Manga,Autores,Comentario
from .forms import UsuarioPersCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied





class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name='Listado'
    
class RegistrarView(CreateView):
   form_class = UsuarioPersCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registrar.html'  

class MangaPageView(ListView):
    template_name = 'mangas.html'
    model = Manga
    context_object_name='Listado1'

class RevistaPageView(ListView):
    template_name = 'revistas.html'
    model = Post
    context_object_name='Listado'

class Descrip_libPageView(ListView):
    template_name = 'descrip_lib.html'
    model = Post
    context_object_name='Listado1'

class AutoresPageView(ListView):
    template_name = 'Autores.html'
    model = Autores
    context_object_name='Listado1'


class DetallePageView(DetailView):
    template_name = 'descAutores.html'
    model = Autores
    context_object_name='Blogs'

class CrearPageView(LoginRequiredMixin,CreateView):
    template_name = 'CrearAutores.html'
    model = Autores
    success_url = reverse_lazy('home')
    fields = 'Nombre','Descripcion','img','Nacionalidad','F_Muerte',
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class UpdatePageView(LoginRequiredMixin,UpdateView):
    template_name = 'editarAutores.html'
    model = Autores
    success_url = reverse_lazy('home')
    fields = 'Nombre','Descripcion','img','Nacionalidad','F_Muerte',
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args,**kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class DeletePageView(LoginRequiredMixin,DeleteView):
    template_name = 'eliminarAutores.html'
    model = Autores
    success_url = reverse_lazy('home')
    context_object_name='Autores'
    login_url = 'login'
    
    def dispatch(self, request, *args,**kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ComentarioCreateView(LoginRequiredMixin,CreateView):
    model = Comentario
    template_name = "comentarioNuevo.html"
    fields = ('comentario',)
    login_url='login'
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        form.instance.autor = self.request.user
        return super().form_valid(form)