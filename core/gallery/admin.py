from django.contrib import admin
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'signature', 'created_at', 'author')
    list_filter = ('id', 'author', 'created_at')
    search_fields = ('author',)
    fields = ('photo', 'author', 'signature', 'created_at')
    readonly_fields = ('id', 'created_at')


admin.site.register(Gallery, GalleryAdmin)
