# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser
from .forms import CustomUserCreationForm


# from app1.models import UploadedFiles 

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'public_visibility', 'birth_year', 'address', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'public_visibility', 'birth_year', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'public_visibility', 'birth_year', 'address', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', 'email', 'address')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')

class UploadedFilesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'visibility', 'cost', 'year_of_publication')
    search_fields = ('title', 'description')
    list_filter = ('visibility', 'year_of_publication')

# admin.site.register(UploadedFiles, UploadedFilesAdmin)
# Now register the new UserAdmin...
admin.site.register(CustomUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

