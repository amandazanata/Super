from django.contrib import admin
from projects.models import Profile
from projects.models import Project

from projects.models import CertifyingInstitution
from projects.models import Certificate


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(CertifyingInstitution)
admin.site.register(Certificate)
