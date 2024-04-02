from django.apps import apps
from django.contrib import admin

from apps.rooms.models import *

app = apps.get_app_config('rooms')  # Replace with your app's name

for model in app.get_models():
    class ModelAdmin(admin.ModelAdmin):
        list_display = [field.name for field in model._meta.fields]  # Display all fields


    admin.site.register(model, ModelAdmin)
