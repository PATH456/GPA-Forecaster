from django.contrib import admin

from .models import Course, GradeComponent, GradeItem, Term


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ["season", "year"]
    list_filter = ["season", "year"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "term", "credits"]
    list_filter = ["term"]
    search_fields = ["code", "name"]


@admin.register(GradeComponent)
class GradeComponentAdmin(admin.ModelAdmin):
    list_display = ["name", "course", "weight_percent", "item_count"]
    list_filter = ["course"]
    search_fields = ["name", "course__code", "course__name"]


@admin.register(GradeItem)
class GradeItemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "component",
        "earned_points",
        "possible_points",
        "is_graded",
    ]
    list_filter = ["component"]
    search_fields = ["name", "component__name", "component__course__code"]
