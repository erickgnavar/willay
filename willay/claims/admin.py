from django.contrib.gis import admin

from .models import Category, Claim


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Claim)
class ClaimAdmin(admin.OSMGeoAdmin):

    list_display = ('address', 'date', 'category',)
    search_fields = ('address',)
    list_filter = ('category', 'verified',)
