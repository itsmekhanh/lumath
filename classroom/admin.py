from django.contrib import admin
from classroom.models import Period, Assignment, Announcement, Test


class AssignmentInline(admin.StackedInline):
    model = Assignment
    extra = 10

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'period','content', 'createtime')
    list_filter = ['createtime']

class PeriodAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['description']})
    ]
    inlines = [AssignmentInline]
    list_display = ('name', 'description')

admin.site.register(Period, PeriodAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Announcement)
admin.site.register(Test)