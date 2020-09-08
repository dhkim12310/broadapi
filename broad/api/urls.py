from django.urls            import path, include
from rest_framework.routers import DefaultRouter
from .views                 import BroadViewSet, CommentView, BroadkDetailAPIView, CommentDetailAPIView

router = DefaultRouter()
router.register(r"broad", BroadViewSet)
router.register(r"broad/<int:pk>", BroadkDetailAPIView)
# router.register(r"broad/<broad:pk>/comment", CommentView)

urlpatterns =[
    path('',include(router.urls)),
    path('broad/<int:broad_pk>/comment',CommentView.as_view(), name = "comment"),
    path("<int:pk>/comment", CommentDetailAPIView.as_view(), name ="comment-detail")

]