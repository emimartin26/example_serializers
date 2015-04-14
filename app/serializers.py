from rest_framework import serializers

class PersonaSerializer(serializers.Serializer):
	nombre =serializers.CharField() 
	tipo_persona = serializers.SlugRelatedField(read_only = True, slug_field = 'nombre')

