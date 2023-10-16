from django.shortcuts import render
from rest_framework import generics
from rest_framework.mixins import Response, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from .models import Certificate as cs
from .models import CertifyingInstitution as ci
from .models import Profile as pf
from .models import Project as pj
from .permissions import IsAuthenticatedor401
from .serializers import CertificateSerializer as css
from .serializers import CertifyingInstitutionSerializer as cis
from .serializers import ProfileSerializer as ps
from .serializers import ProjectSerializer as pjs


class Profile_view_create(generics.ListCreateAPIView):
    queryset = pf.objects.all()  # type: ignore
    serializer_class = ps
    permission_classes = [IsAuthenticatedOrReadOnly]


class Profile_view_crud(generics.RetrieveUpdateDestroyAPIView):
    queryset = pf.objects.all()  # type: ignore
    serializer_class = ps
    permission_classes = [IsAuthenticatedOrReadOnly]
    template_name = "profile_detail.html"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return render(
            request,
            self.template_name,
            {"profile": instance, "serializer": serializer},
        )


class Project_view_create(generics.ListCreateAPIView):
    queryset = pj.objects.all()  # type: ignore
    serializer_class = pjs
    permission_classes = [IsAuthenticatedor401]


class Project_view_crud(generics.RetrieveUpdateDestroyAPIView):
    queryset = pj.objects.all()  # type: ignore
    serializer_class = pjs
    permission_classes = [IsAuthenticatedor401]
    template_name = "profile_detail.html"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Certificate_view(viewsets.ModelViewSet):
    queryset = cs.objects.all()  # type: ignore
    serializer_class = css


class Certificate_view_set(viewsets.ModelViewSet):
    queryset = cs.objects.all()  # type: ignore
    serializer_class = css
