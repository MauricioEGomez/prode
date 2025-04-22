from django.forms import ModelForm
from django import forms
from base.models import Concurso, Participante,FechaProde, Partido, Pronostico

# class ElegirProde(ModelForm)
    
class NuevoProdeForm(ModelForm):
    class Meta:
        model = Concurso
        fields = ['nombre']

class NuevoParticipanteForm(ModelForm):
    class Meta:
        model = Participante
        fields = ['nombre','concursoOrganizacion'] 

class NuevaFechaForm(ModelForm):
    class Meta:
        model = FechaProde
        fields = ['nro', 'apertura', 'cierre', 'concurso']

class PartidoForm(ModelForm):
    class Meta:
        model = Partido
        fields = ['equipo1','resultadoEquipo1','resultadoEquipo2','equipo2',]

class PronosticoForm(ModelForm):
    class Meta:
        model = Pronostico
        fields = ['partido', 'resultadoEquipo1', 'resultadoEquipo2']

class PronosticoForm2(forms.Form):
    partido = forms.CharField(label="Partido:", max_length=200, widget=forms.TextInput(attrs={'class':'input'   }))
    resultado1 = forms.IntegerField(label="Goles Local")    
    resultado2 = forms.IntegerField(label="Goles visitante")