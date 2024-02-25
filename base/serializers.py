from rest_framework import serializers

class NumberConversionSerializer(serializers.Serializer):
    nums = serializers.ListField(child=serializers.CharField())
    file_names = serializers.DictField()