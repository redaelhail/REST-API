from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializer for a name field in hello api view"""

    name = serializers.CharField(max_length=10)
