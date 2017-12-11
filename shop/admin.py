from django.contrib import admin
from .models import Category, Product,Artist, Label

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Artist, ArtistAdmin)

class LabelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Label, LabelAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category','artist','label', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category','artist','label']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
