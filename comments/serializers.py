from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=256)
    amiibo_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    
    class Meta:
        model = Comment
        fields = "__all__"
 
    