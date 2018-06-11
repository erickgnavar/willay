from django.contrib.gis import admin
from django.utils.html import format_html

from .models import Category, Claim


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'marker_icon_preview')
    search_fields = ('name',)

    def marker_icon_preview(self, obj):
        if obj.marker_icon.name:
            return format_html(
                '<img src="{}">',
                obj.marker_icon.url,
            )
        else:
            return ''


@admin.register(Claim)
class ClaimAdmin(admin.OSMGeoAdmin):

    list_display = ('address', 'date', 'category',)
    search_fields = ('address',)
    list_filter = ('category', 'verified',)
