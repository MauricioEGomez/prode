from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from base.models import Deporte, Concurso


# Create your views here.

def index(request):
    concursos = Concurso.objects.all()
    return render(request,'index.html', {
        'concursos': concursos
        })

def about(request):
    return render(request,'about.html')

def sports(request):
    deportes = list(Deporte.objects.values())
    return JsonResponse(deportes, safe=False)    
    
def sport(request, id):
    #print(Deporte.nombre(id=1))
    #deporte = Deporte.objects.get(id=id)
    deporte = get_object_or_404(Deporte,id=id)
    return HttpResponse("Deporte: %s" % deporte.nombre)