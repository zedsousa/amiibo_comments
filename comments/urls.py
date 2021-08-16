from rest_framework.routers import DefaultRouter
from django.urls import include, path
from comments import views

router  = DefaultRouter()

router.register("comment_list", views.CommentViewSet)
urlpatterns = [
    path("", include(router.urls)),
]