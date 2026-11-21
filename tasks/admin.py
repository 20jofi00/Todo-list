from django.contrib import admin

from tasks.models import Tag, Task

admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "is_completed", "created_at", "deadline", "display_tags")
    search_fields = ("title", "description")
    list_filter = ("is_completed", "tags")

    @admin.display(description="Tags")
    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())
