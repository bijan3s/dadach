from django.contrib import admin

from .models import exercises_model,part_model

# Register your models here.

class exercises_admin(admin.ModelAdmin):
    list_display=['name','id']


admin.site.register(exercises_model,exercises_admin)
admin.site.register(part_model)