from django.db import models
from django.contrib.auth.models import User

## Create your models here.
class Deporte(models.Model):
    nombre = models.CharField(max_length=200,default="Sin nombre")

    def __str__(self):
        return(self.nombre)
        
class Torneo(models.Model):
    nombre = models.CharField(max_length=200,default="Sin nombre")
    deporte = models.ForeignKey("Deporte", on_delete=models.CASCADE, null=True)
    inicio = models.DateField(blank=True, null=True)
    fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return(self.deporte.nombre + ", " + self.nombre)

class Organizacion(models.Model):
    nombre = models.CharField(max_length=200, default="Sin nombre")
    concursos =  models.ManyToManyField('Concurso',through='ConcursosOrganizacion')

    def __str__(self):
        return(self.nombre)

class Concurso(models.Model):
    nombre = models.CharField(max_length=200, default="Sin nombre", unique=True)
    activo = models.BooleanField(default=False)
    #organizacion = models.ForeignKey("Organizacion", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return( self.nombre)

class ConcursosOrganizacion(models.Model):
    concurso = models.ForeignKey("Concurso", on_delete=models.CASCADE, null=True)
    organizacion = models.ForeignKey("Organizacion", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return(self.organizacion.nombre + ", " +self.concurso.nombre)

class FechaProde(models.Model):
    nro = models.IntegerField()
    apertura = models.DateField(blank=True)
    cierre = models.DateField(blank=True, null= True)
    concurso = models.ForeignKey("Concurso", on_delete=models.CASCADE, null=True)
    partidos =  models.ManyToManyField('Partido',through='PartidosPorProde')

    def __str__(self):
        return(self.concurso.nombre + ", Fecha:" + str(self.nro))

class Participante(models.Model):
    nombre = models.CharField(max_length=200, default="Sin nombre")
    puntosObtenidos = models.IntegerField(default=0)
    concursoOrganizacion = models.ForeignKey("ConcursosOrganizacion", on_delete=models.CASCADE, null=True)
    partidosPorProde =  models.ManyToManyField('PartidosPorProde',through='Pronostico')
    usuariosPorParticipante =  models.ManyToManyField('Usuario',through='UsuariosPorParticipante')
    def __str__(self):
        return(self.nombre)

class UsuariosPorParticipante(models.Model):
    usuario = models.ForeignKey('usuario', on_delete=models.CASCADE, null=False)
    participante = models.ForeignKey('participante', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return(self.usuario.nombre + ", Equipo:" + self.participante.nombre)

class Usuario(models.Model):
    nombre = models.CharField(max_length=200, default="Sin nombre")
    
    def __str__(self):
        return(self.nombre)

class Equipo(models.Model):
    nombre = models.CharField(max_length=200, default="Ingrese el nombre")

    def __str__(self):
        return(self.nombre)
    
class Grupo(models.Model):
    nombre = models.CharField(max_length=50, default="Sin definir")

    def __str__(self):
        return(self.nombre)

class CategoriaEquipo(models.Model):
    nombre = models.CharField(max_length=50, default="Sin dato")

    def __str__(self):
        return(self.nombre)

class FaseTorneo(models.Model):
    nombre = models.CharField(max_length=200, default="Sin nombre")
#    nroFechaFase = models.CharField(max_length=4, default=" ")
    torneo = models.ForeignKey("torneo", on_delete=models.CASCADE, null=True)
    faseAnterior = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    equipos =  models.ManyToManyField('Equipo',through='EquipoPorFaseTorneo')
    categorias =  models.ManyToManyField('CategoriaEquipo',through='EquipoPorFaseTorneo')
    grupos =  models.ManyToManyField('Grupo',through='EquipoPorFaseTorneo')

    def __str__(self):
        return(self.torneo.nombre + ", " + self.nombre)
    
class EquipoPorFaseTorneo(models.Model):
    faseTorneo = models.ForeignKey("FaseTorneo", on_delete=models.CASCADE, null=False, unique=False)
    equipo = models.ForeignKey("Equipo", on_delete=models.CASCADE, null=False, unique=False)
    categoria = models.ForeignKey("CategoriaEquipo", on_delete=models.CASCADE, null=False, unique=False)
    grupo = models.ForeignKey("Grupo", on_delete=models.CASCADE, null=False, unique=False)

    def __str__(self):
        return(self.faseTorneo.torneo.nombre + ", grupo" + self.grupo.nombre + ", " + self.equipo.nombre+ ", " + self.categoria.nombre)

class Partido(models.Model):
    fecha = models.DateField()
    hora = models.TimeField(blank=True, null=True)
    finalizado = models.BooleanField(default=False)
    estadio = models.CharField(max_length=100, blank=True, null=True)
    equipo1 = models.ForeignKey('EquipoPorFaseTorneo', related_name = 'equipo1', on_delete=models.CASCADE, null=False, unique=False)
    equipo2 = models.ForeignKey('EquipoPorFaseTorneo', related_name = 'equipo2', on_delete=models.CASCADE, null=False, unique=False)
    resultadoEquipo1 = models.SmallIntegerField(blank=True, null=True)    
    resultadoEquipo2 = models.SmallIntegerField(blank=True, null=True)    
    resultadoAdicEquipo1 = models.SmallIntegerField(blank=True, null=True)    
    resultadoAdicEquipo2 = models.SmallIntegerField(blank=True, null=True)    

    def __str__(self):
        return(self.equipo1.faseTorneo.torneo.nombre + ", " + self.equipo1.faseTorneo.nombre + ", " + self.fecha.strftime('%d-%m-%Y') + "  " + self.hora.strftime('%H:%M') + ", " 
               + self.equipo1.equipo.nombre + " vs " + self.equipo2.equipo.nombre)

class PartidosPorProde(models.Model):
    partido = models.ForeignKey("partido", on_delete=models.CASCADE, null=True)
    fechaProde = models.ForeignKey('FechaProde',on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
         return("Fecha: " + str(self.fechaProde.nro) + ", partido " + self.partido.equipo1.equipo.nombre + " vs " + self.partido.equipo2.equipo.nombre)

class Pronostico(models.Model):
    partido = models.ForeignKey('partidosPorProde', on_delete=models.CASCADE, null=True)
    participante = models.ForeignKey('participante', on_delete=models.CASCADE, null=True)
    resultadoEquipo1 = models.SmallIntegerField(null=True)    
    resultadoEquipo2 = models.SmallIntegerField(null=True)    
    resultadoAdicEquipo1 = models.SmallIntegerField(blank=True, null=True)    
    resultadoAdicEquipo2 = models.SmallIntegerField(blank=True, null=True)    
