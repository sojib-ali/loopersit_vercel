from django.contrib import admin
from .models import FAQ, Member, Portfolio, ProjectSummary


admin.site.register(FAQ)
admin.site.register(ProjectSummary)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'order']
    list_filter = ['role']
    list_editable = ['order']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'link', 'order']
    list_editable = ['order']