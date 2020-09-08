from rest_framework             import generics, mixins
from rest_framework.viewsets    import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.generics    import get_object_or_404
from rest_framework.exceptions  import ValidationError

from .permissins                import IsAdminUserOrReadOnly,IsReviewAuthorOrReadOnly
from broad.api.serializers      import BroadSerializer,CommentSerializer
from broad.models               import Broad,Comment

class BroadViewSet(ModelViewSet):
    queryset            = Broad.objects.all()
    serializer_class    = BroadSerializer
    permission_classes  = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BroadkDetailAPIView(ModelViewSet):
    queryset            = Broad.objects.all()
    serializer_class    = BroadSerializer
    permission_classes  = [IsReviewAuthorOrReadOnly]


class CommentView(generics.ListCreateAPIView):
    queryset            = Comment.objects.all()
    serializer_class    = CommentSerializer
    permission_classes  = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        broad_pk        = self.kwargs.get("broad_pk")
        broad           = get_object_or_404(Broad, pk = broad_pk)
        user            = self.request.user
        review_queryset = Comment.objects.filter(broad = broad,
                                                user = user)
        
        if review_queryset.exists():
            raise ValidationError("You Have Already Commented this Broad!")

        serializer.save(broad=broad,user =user)

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset             = Comment.objects.all()
    serializer_class     = CommentSerializer
    permission_classes   = [IsReviewAuthorOrReadOnly]
