from django.contrib import admin

from .models import Program, ProgramType, HomePage, Navbar, Logo, AdmissionSidebarItem

# Register your models here.
admin.site.register(Program)
admin.site.register(ProgramType)
admin.site.register(HomePage)
admin.site.register(Navbar)
admin.site.register(Logo)
admin.site.register(AdmissionSidebarItem)