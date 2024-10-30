from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'social_link', 'github_id')  # Поля, которые будут отображаться в списке пользователей
    search_fields = ('username', 'email')  # Поля, по которым можно осуществлять поиск
    ordering = ('username',)  # Порядок сортировки пользователей по умолчанию


admin.site.register(CustomUser, CustomUserAdmin)
