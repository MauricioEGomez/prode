from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NuevoProdeForm, NuevoParticipanteForm, NuevaFechaForm, PartidoForm, PronosticoForm
from base.models import Concurso, FechaProde, Participante, Usuario, UsuariosPorParticipante, ConcursosOrganizacion, PartidosPorProde, Partido, Pronostico

# Create your views here.

def participantes_usuario(request):
    usuario = Usuario.objects.get(nombre=request.user)

    # busco los equipos en donde el usuario figura
    participantesporusuario_queryset = UsuariosPorParticipante.objects.filter(usuario=usuario)
    # print("participantesporusuario_queryset.values_list('participante') "+str(participantesporusuario_queryset.values_list('participante_id')))

    # obtengo los participantes en donde los participantesporusuario_queryset figuran
    participantes_queryset = Participante.objects.filter(
        id__in = participantesporusuario_queryset.values_list('participante')
    )
    
    return participantes_queryset

@login_required
def prodes(request):
    # obtengo los equipos en donde figura el usuario 
    participantes_queryset = participantes_usuario(request)

    # obtengo los ConcursosOrganizacion en donde los participantes figuran
    concursos_organizacion_queryset = ConcursosOrganizacion.objects.filter(
        id__in = participantes_queryset.values_list('concursoOrganizacion'),
    )
    # print("concursos_organizacion_queryset "+str(concursos_organizacion_queryset))

    # obtengo los ConcursosOrganizacion en donde los participantes figuran
    prodes = Concurso.objects.filter(
        id__in = concursos_organizacion_queryset.values_list('concurso_id'),
        activo = True
    )
    # print("prodes "+str(prodes))

    return render(request, 'prodes.html', {
        "prodes":prodes})

@login_required
def nuevo_prode(request):

    if request.method == 'GET':
        # print('mostrando formulario')
        return render(request, 'nuevo_prode.html', {
                'form': NuevoProdeForm,
        })
    else:
        try: 
            # print(request.POST) 
            nuevo_prode = NuevoProdeForm(request.POST)   
            nuevo_prode.save()
            return redirect('prodes')
        except ValueError:
            return render(request, 'nuevo_prode.html', {
                'form': NuevoProdeForm,
                'error': "Ingresó un dato erróneo"
            })

@login_required
def fecha_prode(request, id):
    fecha = get_object_or_404(FechaProde,id=id)
    return render(request, 'fecha_prode.html', {
            "fecha":fecha})

@login_required
def fechas_prode(request, concurso_id):
    # fechasProde = FechaProde.objects.all()
    # fechasProde = get_list_or_404(FechaProde.objects.concurso_id==concurso_id)

    # busco el nombre para mostrarlo como título
    nombre_prode = Concurso.objects.get(id=concurso_id)
    print(nombre_prode)
    fechasProde = FechaProde.objects.filter(concurso_id=concurso_id)
    return render(request, 'fechas_prode.html', {
        "nombre_prode":nombre_prode,
        "fechas":fechasProde,
        })

@login_required
def nueva_fecha(request):

    if request.method == 'GET':
        # print('mostrando formulario')
        return render(request, 'nueva_fecha.html', {
                'form': NuevaFechaForm,
        })
    else:
        try: 
            # print('acá' + str(request.POST))
            nueva_fecha = NuevaFechaForm(request.POST)   
            nueva_fecha.save()
            print(nueva_fecha)
            return redirect('prodes')
        except ValueError:
            return render(request, 'nueva_fecha.html', {
                'form': NuevaFechaForm,
                'error': "Ingresó un dato erróneo"
            })

@login_required
def partidos_fecha_prode(request, fecha_id):
    partidosPorProde_queryset = PartidosPorProde.objects.filter(fechaProde_id=fecha_id)
    #print(partidosPorProde_queryset)

    partidos = Partido.objects.filter(id__in = partidosPorProde_queryset.values_list('partido_id'))
    return render(request, 'partidos.html', {
        "partidos":partidos,
        })

@login_required
def nuevo_pronostico(request ):

    if request.method == 'GET':
        # print('mostrando formulario')
        return render(request, 'nuevo_pronostico.html', {
                'form': PronosticoForm,
        })
    else:
        try: 
            # print(request.POST) 
            nuevo_prode = PronosticoForm(request.POST)   
            nuevo_prode.save()
            return redirect('prodes')
        except ValueError:
            return render(request, 'nuevo_pronostico.html', {
                'form': PronosticoForm,
                'error': "Ingresó un dato erróneo"
            })
     
@login_required
def participantes(request):
    participantes = Participante.objects.all()
    return render(request, 'participantes.html', {
        "participantes":participantes})

@login_required
def nuevo_participante(request):

    if request.method == 'GET':
        # print('mostrando formulario')
        return render(request, 'nuevo_participante.html', {
                'form': NuevoParticipanteForm,
        })
    else:
        try: 
            # print(request.POST) 
            nuevo_participante = NuevoParticipanteForm(request.POST)   
            nuevo_participante.save()
            return redirect('participantes')
        except ValueError:
            return render(request, 'nuevo_participante.html', {
                'form': NuevoParticipanteForm,
                'error': "Ingresó un dato erróneo"
            })

@login_required
def pronosticos(request):
    usuario = Usuario.objects.get(nombre=request.user)

    # busco los equipos en donde el usuario figura
    participantesporusuario_queryset = UsuariosPorParticipante.objects.filter(usuario=usuario)
    # print("participantesporusuario_queryset.values_list('participante') "+str(participantesporusuario_queryset.values_list('participante_id')))

    # obtengo los Participantes en donde los participantesporusuario_queryset figuran
    participantes_queryset = Participante.objects.filter(
        id__in = participantesporusuario_queryset.values_list('participante')
    )
    # print("participantes_queryset.values_list('nombre') "+str(participantes_queryset.values_list('nombre')))
    # print("participantes_queryset "+str(participantes_queryset))

    # obtengo los ConcursosOrganizacion en donde los participantes figuran
    pronosticos = Pronostico.objects.filter(
        id__in = participantes_queryset.values_list('id')
    )
    pronosticos = Pronostico.objects.all()
    return render(request, 'pronosticos.html', {
        "pronosticos":pronosticos})

@login_required
def partido(request, id):
    # obtengo los ConcursosOrganizacion en donde los participantes figuran
    partido = Partido.objects.get(id = id)

    if request.method == 'POST':
        form = PartidoForm(request.POST, instance=partido)

        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            return redirect('partidos')
            # return render(request, 'partido.html', {
            # "form":form,
            # 'partido': partido},
            # )
    else:
        form = PartidoForm(instance=partido)
        return render(request, 'partido.html', {
        "form":form,
        'partido': partido},
        )

@login_required
def partidos(request):
    # obtengo los ConcursosOrganizacion en donde los participantes figuran
    partidos = Partido.objects.all()
    return render(request, 'partidos.html', {
        "partidos":partidos})