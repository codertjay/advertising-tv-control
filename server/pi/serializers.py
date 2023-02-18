from rest_framework import serializers

from .models import PiDevice


class PiDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiDevice
        fields = "__all__"
