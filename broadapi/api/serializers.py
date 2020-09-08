from rest_framework import serializers
from broadapi.models import Broad, Profile, Comment

class CommentSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Comment
        exclude = ("broad",)
        # fields = "__all__"


class BroadSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many= True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    hits = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Broad
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Profile
        fields = "__all__"



# class BroadTitleViewSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Broad
#         fields = "__all__"
        # fields = ("id","title","hits","created_at",)
