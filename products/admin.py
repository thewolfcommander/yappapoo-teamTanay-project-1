from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *


class ProductImageInline(admin.TabularInline):
    """
    Tabular Inline for Product Images so that it can come as inline for Products
    """
    model = ProductImage
    extra = 1


class ProductSizeInline(admin.TabularInline):
    """
    Tabular INline for Product Available sizes
    """
    model = ProductSizes
    extra = 1


class ProductReviewInline(admin.TabularInline):
    """
    Tabular Inline for product reviews
    """
    model = ProductReview
    extra = 0


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    """
    Admin Configuration for Category Model
    """
    list_display = ['id', 'name', 'slug', 'added', 'active']
    list_filter = ['added', 'updated', 'active']
    search_fields = ['name', 'description']


@admin.register(Seller)
class SellerAdmin(ImportExportModelAdmin):
    """
    Admin Configuration for Sellers
    """
    list_display = ['id', 'user', 'phone_number', 'company_name', 'state', 'postal']
    list_filter = ['country', 'state']
    search_fields = ['company_name']


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    """
    Admin Configuration for Products
    """
    list_display = ['id', 'name', 'slug', 'added', 'active', 'gross_price', 'discount_price']
    list_filter = ['added', 'updated', 'active', 'seller']
    search_fields = ['name', 'description']
    inlines = [ProductImageInline, ProductSizeInline, ProductReviewInline]