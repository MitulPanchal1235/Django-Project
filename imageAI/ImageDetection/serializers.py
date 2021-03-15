from rest_framework import serializers
class Serializerpy(serializers.Serializer):
    image_file = serializers.ImageField()
    xml_file = serializers.FileField()
