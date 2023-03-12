from django.urls import path
from rest_framework.routers import DefaultRouter

from flights_app.views.flights import FlightsViewSet

# automatically defining urls for MoviesViewSet
router = DefaultRouter()
router.register('', FlightsViewSet)


urlpatterns = []

# adding movies urls to urlpatterns
urlpatterns.extend(router.urls)
