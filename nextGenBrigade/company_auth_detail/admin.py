# from django.contrib import admin
# from .models import *
# # Register your models here.
# from django.contrib import admin
# from .models import CustomCompanyUser

# # @admin.register(CustomCompanyUser)
# # class CustomCompanyUserAdmin(admin.ModelAdmin):
# #     def delete_model(self, request, obj):
# #         # e.g. obj.profiles.all().delete()
# #         super().delete_model(request, obj)
# admin.site.register(CustomCompanyUser)

from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class CustomCompanyUserAdmin(admin.ModelAdmin):
    # ... your existing config ...

    def delete_model(self, request, obj):
        # delete any Admin log entries first
        LogEntry.objects.filter(user_id=obj.pk).delete()
        super().delete_model(request, obj)