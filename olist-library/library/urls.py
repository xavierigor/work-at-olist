from django.urls import path, include
from rest_framework import routers
from library import views


app_name = "library"

router = routers.DefaultRouter()
router.register(r"authors", views.AuthorViewSet, basename="authors")
router.register(r"books", views.BookViewSet, basename="books")


urlpatterns = [
    path("", include(router.urls))
]
