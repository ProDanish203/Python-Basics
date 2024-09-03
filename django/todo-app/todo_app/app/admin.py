from django.contrib import admin
from .models import Todo, TodoReview, Category, Profile


# Register your models here.
class TodoReviewInline(admin.TabularInline):
    model = TodoReview
    extra = 1


class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "completed", "created_at"]
    inlines = [TodoReviewInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    filter_horizontal = ["todos"]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "bio"]


admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile, ProfileAdmin)
