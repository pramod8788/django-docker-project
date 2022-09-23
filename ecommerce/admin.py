from django.contrib import admin
from . import models
from django.contrib.admin import SimpleListFilter

admin.site.site_url = '/seller'
admin.site.site_header = 'Administration'
admin.site.site_title = 'Seller'

# Register your models here.
class LessThanFiveFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = "Custom Id"

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'filter-by-custom-id'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (('lt500', 'Less than 500'), ('gt500', 'Greater than 500'))

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == 'lt500':
            return queryset.filter(id__lt=500)
        
        if self.value() == 'gt500':
            return queryset.filter(id__gt=500)


class ElectronicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("prod_name",)}
    list_filter = (LessThanFiveFilter, 'type', 'seller_name')

class FashionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("prod_name",)}
    list_filter = ('type', 'seller_name',)

class HomeDecorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("prod_name",)}
    list_filter = ('type', 'seller_name',)

class MobileAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("prod_name",)}
    list_filter = ('type', 'seller_name',)


admin.site.register(models.Address)
admin.site.register(models.Contact)
admin.site.register(models.Carousel)
admin.site.register(models.Category)
admin.site.register(models.Cart)
admin.site.register(models.Seller)
admin.site.register(models.Electronic, ElectronicAdmin)
admin.site.register(models.Fashion, FashionAdmin)
admin.site.register(models.HomeDecor, HomeDecorAdmin)
admin.site.register(models.Mobile, MobileAdmin)