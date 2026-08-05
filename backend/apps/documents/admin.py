from django.contrib import admin

from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "owner",
        "category",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "owner__username",
        "owner__email",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )