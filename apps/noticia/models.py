from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    publicado = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(null=True, blank=True, upload_to='noticia',default='noticia/default.jpg')

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
        
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()


class Comentario(models.Model):
    # usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=Usuario)
    Noticia = models.ForeignKey(Noticia, related_name='Comentarios', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    texto = models.TextField()
    approved_comment = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return '%s - %s' % (self.Noticia.titulo, self.nombre)
    
    class Meta:
        ordering = ('-fecha',)