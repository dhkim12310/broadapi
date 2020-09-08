from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet, ViewSet
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from broadapi.api.pagination import Pagination
from broadapi.models import (Profile,
                            Comment,
                            Broad)
from broadapi.api.serializers import (ProfileSerializer,
                                     CommentSerializer,
                                     BroadSerializer)


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class BroadListCreateAPIView(ModelViewSet):
    queryset = Broad.objects.all().order_by("-id")
    serializer_class = BroadSerializer
    pagination_class = Pagination
    # filter_backends = [SearchFilter]
    # Search_fields = ["title","user"]

class BroadDetailAPIView(ModelViewSet):
    queryset = Broad.objects.all()
    serializer_class = BroadSerializer

    def perform_create(self,serializer):
        queryset = Profile.objects.all()
        username = self.request.query_params.get("username",None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset

class CommentCreateAPIView(generics.CreateAPIView):
# class CommentCreateAPIView(ViewSet):
    queryset = Comment.objects.all().order_by("-id")
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        broad_pk = self.kwargs.get("broad_pk")
        broad = get_object_or_404(Broad, pk = broad_pk)
        serializer.save(broad=broad)
    
        # comment_user = self.request.user
        # comment_queryset = Comment.objects.filter(broad = broad,
        #                                             user = comment_user)
        
        # if comment_queryset.exists():
        #     raise ValidationError("You Have Already Commented this Broad!")

        # serializer.save(broad = broad, user = comment_user)

# class CommentDetailAPIView(ModelViewSet):
#     queryset = Comment.objects.all().order_by("-id")
#     serializer_class = CommentSerializer

