from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from flights_app.models import Order
from flights_app.serializers.orders import OrderSerializer


# only logged-in users can create a review
# only user that created a review can update/delete it



class OrdersPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'PATCH']:
            return request.user.is_staff
        return True


class OrdersViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    permission_classes = [OrdersPermissions]
    # authentication_classes = [JWTAuthentication]

    # we need different serializers for different actions
    serializer_class = OrderSerializer

