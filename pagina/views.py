from django.shortcuts import render
from .models import Auto, Evento, Sucursal, Comentario

def inicio(request):
    return render(request, 'pagina/index.html')
        
from .models import Producto

def productos(request):
    lista_productos = Producto.objects.all()
    return render(request, 'pagina/productos.html', {'productos': lista_productos})

def autos(request):
    lista_autos = Auto.objects.all()
    return render(request, 'pagina/autos.html', {'autos': lista_autos})

def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'pagina/eventos.html', {'eventos': eventos})

def sucursales(request):
    lista_sucursales = Sucursal.objects.all()
    return render(request, 'pagina/sucursales.html', {'sucursales': lista_sucursales})


def comentarios(request):
    if request.method == "POST":
        autor = request.POST.get("autor")
        texto = request.POST.get("texto")

        Comentario.objects.create(
            autor=autor,
            texto=texto
        )

    lista_comentarios = Comentario.objects.all().order_by('-fecha')

    return render(request, 'pagina/comentarios.html', {'comentarios': lista_comentarios})