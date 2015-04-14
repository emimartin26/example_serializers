from django.db import models

# Create your models here.

class TipoPersona(models.Model):
	nombre = models.CharField(max_length = 150)


class Persona(models.Model):
	nombre = models.CharField(max_length = 150)
	tipo_persona = models.ForeignKey(TipoPersona)


