from Admin_panel.models import App
from rest_framework import serializers

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'app_name', 'download_link', 'points']