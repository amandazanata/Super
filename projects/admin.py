from django.contrib import admin
from projects.models import Profile
from projects.models import Project

from projects.models import CertifyingInstitution
from projects.models import Certificate


class CertificateInline(admin.StackedInline):
    model = Certificate


class CertifyingInstitutionAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(CertifyingInstitution, CertifyingInstitutionAdmin)
admin.site.register(Certificate)
