from django.urls import path
from .views import HomePageView,RevistaPageView,MangaPageView,Descrip_libPageView,AutoresPageView,DetallePageView,CrearPageView,UpdatePageView,DeletePageView,RegistrarView,ComentarioCreateView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns=[
        path('',HomePageView.as_view(),name='home'),
     path('mangas',MangaPageView .as_view(),name='mangas'),
      path('revistas',RevistaPageView.as_view(),name='revistas'),
      path('descrip_lib',Descrip_libPageView.as_view(),name='descrip_lib'),
      path('Autor',AutoresPageView.as_view(),name='Autores'),
       path('Nombre/<int:pk>/editar',DetallePageView.as_view(),name='descAutores'),
    path('Nuevo/Autor',CrearPageView.as_view(),name='CrearAutores'),
     path('Nombre/<int:pk>/Update',UpdatePageView.as_view(),name='EditAutores'),
      path('Nombre/<int:pk>/delet',DeletePageView.as_view(),name='deleteAutores'),
    path('registrar/', RegistrarView.as_view(),name='registrar'),
      path('Comentarios/<int:libroComent>',ComentarioCreateView.as_view(),name='comentarioNuevo'),
   
    path('password_reset/', PasswordResetView.as_view(
        template_name='registration/password_reset.html'
    ),name='password_reset'),

   path('password_reset_done/', PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ),name='password_reset_done'),

   path('usuarios/password_reset_confirm/<u1db64>/<token>', PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ),name='password_reset_confirm'),

path('usuarios/password_reset_complete', PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ),name='password_reset_complete'),

]
