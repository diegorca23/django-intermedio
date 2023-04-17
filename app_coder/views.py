from datetime import datetime

from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context, loader



def primer_template(request):
    archivo = open(r'/mnt/c/Users/diego/OneDrive/Escritorio/intermedio_local/templates/primer_template.html', 'r')
    template = Template(archivo.read())
    archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)


def segundo_template(request):
    dt = datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    
    template = loader.get_template(r'segundo_template.html')
    
    datos = {'fecha': dt_formateado}
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)


def tercer_template(request):
    datos = {'nombre': 'Pepe'}
    # template = loader.get_template(r'prueba_render.html')
    # template_renderizado = template.render(datos)
    # return HttpResponse(template_renderizado)

    # return render(request, r'prueba_render.html')
    return render(request, r'tercer_template.html', datos)