from django.urls import path, include
from rest_framework.routers import DefaultRouter

from broadapi.api.views import (BroadListCreateAPIView,
                                BroadDetailAPIView,
                                CommentCreateAPIView,
                                ProfileViewSet)

router = DefaultRouter()
router.register(r"broad/<int:pk>",BroadDetailAPIView)
router.register(r"profile",ProfileViewSet)
router.register(r"broad",BroadListCreateAPIView)
# router.register(r"broad/<int:broad_pk>/comment",CommentCreateAPIView)

urlpatterns = [
    path("",include(router.urls)),
    # path("broad/",BroadListCreateAPIView.as_view(), name = "broad-list")
    path("broad/<int:broad_pk>/comment/",CommentCreateAPIView.as_view(),name = "comment-list")
]