from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer

from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import viewsets

class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = "__all__"
