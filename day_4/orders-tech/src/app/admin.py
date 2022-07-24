from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin

"""
from .models.user import User, Profile
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_client', 'is_verified')
    list_filter = ('is_client', 'is_verified')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'country')
    list_filter = ('user', 'phone_number', 'address', 'country')
    search_fields = ('user', 'phone_number', 'address', 'country')
    ordering = ('user', 'phone_number', 'address', 'country')

admin.site.register(User, CustomUserAdmin) 
"""  