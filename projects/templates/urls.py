from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    r"certificates", views.Certificate_view
)
router.register(
    r"certifying-institutions",
    views.Certificate_view_set
)


urlpatterns = [
    path(
        "profiles/",
        views.Profile_view_create.as_view(),
        name="profile-list-crate",
    ),
    path(
        "profiles/<int:pk>/",
        views.Profile_view_crud.as_view(),
        name="profile-retrieve-update-destroy",
    ),
    path(
        "projects/",
        views.Project_view_create.as_view(),
        name="project-list-crate",
    ),
    path(
        "projects/<int:pk>/",
        views.Project_view_crud.as_view(),
        name="project-retrieve-update-destroy",
    ),
    path('', include(router.urls)),
]
