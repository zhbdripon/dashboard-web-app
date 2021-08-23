from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()

from accounts.models import Profile
from accounts.serializers import ProfileSerializer
from accounts.permissions import IsOwnerOrAdmin


class ProfileList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Profile.objects.all()
        else:
            return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        obj = get_object_or_404(Profile.objects.all(), user = self.kwargs['pk'] )
        self.check_object_permissions(self.request, obj)
        return obj