from rest_framework import serializers
from notes.models import NOTE
from tracker_chart.models import testCHART #""", testCHART_DATA"""
from url_data.models import URL_DATA

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        created_at = serializers.ReadOnlyField()

        model   = NOTE
        fields  = ['id', 'content', 'created_at'] 

class ChartSerializer(serializers.ModelSerializer):
    chart_data = serializers.StringRelatedField(many=True)
    class Meta:
        created_at = serializers.ReadOnlyField()

        model   = testCHART
        fields  = ['id', 'chart_name', 'description', 'chart_data', 'created_at']

"""class ChartDataSerializer(serializers.ModelSerializer):
    class Meta:
        created_at = serializers.ReadOnlyField()

        model   = testCHART_DATA
        fields  = ['id', 'chart', 'data_name', 'data', 'created_at']"""

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        created_at = serializers.ReadOnlyField()

        model = URL_DATA
        fields = ['id', 'title', 'url_link', 'created_at']