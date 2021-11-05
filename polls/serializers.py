from rest_framework import serializers
from .models import Poll

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = (
            'id', 'title', 'body', 'created_at', 'updated_at'
        )

