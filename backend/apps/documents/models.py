from django.conf import settings
from django.db import models


class Document(models.Model):

    CATEGORY_CHOICES = [
        ("personal", "Personal"),
        ("education", "Education"),
        ("professional", "Professional"),
        ("certificate", "Certificate"),
        ("identity", "Identity"),
        ("other", "Other"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="other",
    )

    file = models.FileField(
        upload_to="documents/%Y/%m/",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Document"
        verbose_name_plural = "Documents"
