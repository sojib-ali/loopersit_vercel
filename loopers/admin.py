from django.contrib import admin
from .models import Service, ServiceOffer, SubService, Review, Page, Pricing, PriceFeature

# Register your models here.

class ServiceOfferInline(admin.TabularInline):
    model = ServiceOffer
    extra = 0

@admin.register(SubService)
class SubServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'service', 'order']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['service',]
    list_editable = ['order']


class SubServiceInline(admin.StackedInline):
    model = SubService
    extra = 0


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name' ,'description', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ServiceOfferInline, SubServiceInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'order']
    list_editable = ['order']

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'link_on_footer']
    list_editable = ['link_on_footer']
    prepopulated_fields = {'slug': ('title',)}

class PriceFeatureInline(admin.TabularInline):
    model = PriceFeature
    extra = 0

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_range', 'order']
    list_editable = ['order',]
    inlines = [PriceFeatureInline,]