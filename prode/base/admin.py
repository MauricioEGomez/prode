from django.contrib import admin
from .models import CategoriaEquipo, Concurso, ConcursosOrganizacion, Deporte, Equipo, EquipoPorFaseTorneo, FaseTorneo, FechaProde, Grupo, Organizacion, Participante, Partido, PartidosPorProde, Torneo, Usuario, UsuariosPorParticipante, Pronostico

# Register your models here.
admin.site.register(CategoriaEquipo)
admin.site.register(Concurso)
admin.site.register(ConcursosOrganizacion)
admin.site.register(Deporte)
admin.site.register(Equipo)
admin.site.register(EquipoPorFaseTorneo)
admin.site.register(FaseTorneo)
admin.site.register(FechaProde)
admin.site.register(Grupo)
admin.site.register(Organizacion)
admin.site.register(Participante)
admin.site.register(Partido)
admin.site.register(PartidosPorProde)
admin.site.register(Pronostico)
admin.site.register(Torneo)
admin.site.register(Usuario)
admin.site.register(UsuariosPorParticipante)



