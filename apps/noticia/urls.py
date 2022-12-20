from django.urls import path
from .views import NoticiaListView, NoticiaDetalleView, AddComentarioView

urlpatterns = [
    path("noticias/", NoticiaListView.as_view()),
    path('detalle/<int:pk>', NoticiaDetalleView.as_view(), name='detalle'),
    path('detalle/<int:pk>/add_comment/', AddComentarioView.as_view(), name='add_comment'),
]