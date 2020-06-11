from django.urls import path, include
from rest_framework import routers
from library import views


router = routers.DefaultRouter()
router.register(r"authors", views.AuthorViewSet)
router.register(r"books", views.BookViewSet)


urlpatterns = [
    path("", include(router.urls))
]
