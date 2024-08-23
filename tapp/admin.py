from django.contrib import admin
from .models import Task, Author, Tag

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date', 'status']
    search_fields = ['title', 'description']
    list_filter = ['status', 'author']

    def mark_as_completed(TaskAdmin, request, queryset):
        queryset.update(status='due')

    mark_as_completed.short_description = 'Complete selected tasks'
        
    actions = ['mark_as_completed']    


admin.site.register(Task, TaskAdmin)
admin.site.register(Author)
admin.site.register(Tag)


admin.site.site_header = 'Todo App'
admin.site.site_title = 'TodoApp'