from django.contrib import admin
from .models import (
    ProductCategory,
    Product,
    SubProduct,
    Advantage,
    CommitmentPoint,
    Blogs,
    Author,
    BlogCategory,
    Review,
)


# -----------------------------
# Inlines for Product
# -----------------------------
class SubProductInline(admin.TabularInline):
    model = SubProduct
    extra = 1
    fields = ("title", "description", "image")


class AdvantageInline(admin.TabularInline):
    model = Advantage
    extra = 1
    fields = ("title", "point")


class CommitmentInline(admin.TabularInline):
    model = CommitmentPoint
    extra = 1
    fields = ("point",)


# -----------------------------
# Product Admin
# -----------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("meta_title", "category", "created_at", "updated_at")
    search_fields = ("meta_title", "category__name")
    inlines = [SubProductInline, AdvantageInline, CommitmentInline]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


# -----------------------------
# Blog Admin
# -----------------------------
@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("H1",)
    search_fields = ("H1", "meta_title", "content", "slug")
    ordering = ("-id",)

    class Media:
        js = [
            "ckeditor/ckeditor-init.js",
            "ckeditor/ckeditor/ckeditor.js",
        ]


# -----------------------------
# Author Admin
# -----------------------------
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")
    list_filter = ("position",)
    ordering = ("name",)


# -----------------------------
# Blog Category Admin
# -----------------------------
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


# -----------------------------
# Review Admin
# -----------------------------
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "review")
    search_fields = ("name", "review")
