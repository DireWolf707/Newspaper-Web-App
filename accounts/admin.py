from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUser
from django.contrib import admin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','username','age','is_staff',)
    
    fieldsets = UserAdmin.fieldsets + (
        ('Age', {'fields': ('age',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','password1', 'password2'),
        }),
    )

admin.site.register(CustomUser,CustomUserAdmin)