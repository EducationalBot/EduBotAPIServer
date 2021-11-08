from rest_framework import viewsets, mixins
from user.models import User
from user.permissions import IsUserOrReadOnly
from user.api.serializer import UserSerializer

__all__ = [
    'UserViewSet'
]

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)
