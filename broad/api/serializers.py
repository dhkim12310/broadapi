from rest_framework import serializers
from broad.models   import Broad, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)

    class Meta:
        model            = Comment
        fields           = "__all__"
        read_only_fields = ['broad']

class BroadSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)
    hits    = serializers.StringRelatedField(read_only = True)
    user    = serializers.StringRelatedField(read_only = True)

    class Meta:
        model    = Broad
        fields   = "__all__"
    
