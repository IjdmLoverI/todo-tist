from django.contrib import admin

from todo.models import Tag, Task


admin.site.register(Task)
admin.site.register(Tag)
