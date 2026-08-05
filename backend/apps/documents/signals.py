from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from .models import Document


@receiver(post_delete, sender=Document)
def delete_document_file_on_delete(
    sender,
    instance,
    **kwargs,
):
    """
    Delete the physical file when
    a Document object is deleted.
    """

    if instance.file:
        instance.file.delete(
            save=False,
        )


@receiver(pre_save, sender=Document)
def delete_old_file_on_update(
    sender,
    instance,
    **kwargs,
):
    """
    Delete the old physical file when
    a document is updated with a new file.
    """

    if not instance.pk:
        return

    try:
        old_document = Document.objects.get(
            pk=instance.pk,
        )
    except Document.DoesNotExist:
        return

    old_file = old_document.file
    new_file = instance.file

    if (
        old_file
        and old_file.name
        and old_file.name != new_file.name
    ):
        old_file.delete(
            save=False,
        )
