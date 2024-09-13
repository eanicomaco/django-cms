from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from contas.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('name','cpf','email','is_active','is_staff',)
    list_filter = ('is_active', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Personal info',{'fields':('name','cpf')}),
        ('Permissions',{'fields': ('is_active', 'is_staff', 'is_superuser','groups','user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','name','cpf','password1','password2',)
        }),
    )
    search_fields = ('email', 'name', 'cpf')
    ordering = ('name',)
    readonly_fields = ('last_login',)
