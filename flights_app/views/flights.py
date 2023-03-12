from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, SAFE_METHODS

from flights_app.models import Flight
from flights_app.serializers.flights import FlightSerializer


class FlightsPaginationClass(PageNumberPagination):
    page_size = 3


class FlightsPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'PATCH']:
            return request.user.is_staff
        return True


class FlightsViewSet(viewsets.ModelViewSet):

    queryset = Flight.objects.all()
    permission_classes = [FlightsPermissions]
    # authentication_classes = [JWTAuthentication]

    # we need different serializers for different actions
    serializer_class = FlightSerializer

    # pagination is defined either using DEFAULT_PAGINATION_CLASS in settings.py
    # or you can specify one here
    # pagination_class = MoviesPaginationClass

