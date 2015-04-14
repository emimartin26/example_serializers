from django.shortcuts import render
from django.http import HttpResponse
import json
from .serializers import PersonaSerializer
from .models import Persona, TipoPersona

# Create your views here.

def home(request):
	tipo = TipoPersona(nombre='humano')
	tipo.save()
	p = Persona(nombre = 'Emiliano', tipo_persona = tipo)
	p.save()
	serializer = PersonaSerializer(p, many = False)
	return HttpResponse(json.dumps(serializer.data),content_type="application/json")
	
