from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.AboutLogin)
class AboutLoginAdmin(admin.ModelAdmin):
    list_display = ('id',)

    def has_add_permission(self, request):
        if models.AboutLogin.objects.all().exists():
            return False
        return True


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
