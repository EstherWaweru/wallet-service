# from models import User
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.FloatField()
    created = serializers.CharField(max_length = 5)
