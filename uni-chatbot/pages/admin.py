from django.contrib import admin

from .models import (
    AdmissionReqBullet,
    AdmissionSidebarItem,
    ContactPage,
    Department,
    DepartmentPage,
    Faculty,
    FundingPage,
    GraduateAdmissionPage,
    HomePage,
    LanguageReqExemptionBullet,
    Logo,
    Navbar,
    OnlineCoursesBullet,
    OnlineCoursesPage,
    Program,
    ProgramType,
    UndergraduateAddmissionReqPage,
)

# Register your models here.
admin.site.register(Program)
admin.site.register(ProgramType)
admin.site.register(HomePage)
admin.site.register(Navbar)
admin.site.register(Logo)
admin.site.register(AdmissionSidebarItem)
admin.site.register(FundingPage)
admin.site.register(ContactPage)


# Register bullet points inline so they can be edited directly within the main page form
class LanguageExemptionInline(admin.TabularInline):
    model = LanguageReqExemptionBullet
    extra = 1


@admin.register(UndergraduateAddmissionReqPage)
class UndergraduateAdmissionAdmin(admin.ModelAdmin):
    inlines = [LanguageExemptionInline]


# Register bullet points inline with Graduate Page
class GraduateRequirementInline(admin.TabularInline):
    model = AdmissionReqBullet
    extra = 1


@admin.register(GraduateAdmissionPage)
class GraduateAdmissionAdmin(admin.ModelAdmin):
    inlines = [GraduateRequirementInline]


# Register bullet points inline with Online Course Page
class OnlineCoursesBulletInline(admin.TabularInline):
    model = OnlineCoursesBullet
    extra = 1


@admin.register(OnlineCoursesPage)
class OnlineCoursesAdmin(admin.ModelAdmin):
    inlines = [OnlineCoursesBulletInline]


# Register Faculty and Departments inline
class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 1
    ordering = ["order"]


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)
    ordering = ["order"]
    inlines = [DepartmentInline]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "faculty", "order")
    list_editable = ("order",)
    ordering = ["faculty", "order"]


# Register Department pages
@admin.register(DepartmentPage)
class DepartmentPageAdmin(admin.ModelAdmin):
    list_display = ("page_title", "department", "main_heading")
    search_fields = ("page_title", "department__name", "main_heading")
    list_filter = ("department",)
