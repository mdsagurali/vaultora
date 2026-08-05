from django import forms
from PIL import Image

from .models import Document


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document

        fields = [
            "title",
            "description",
            "category",
            "file",
        ]

    def clean_file(self):
        file = self.cleaned_data.get("file")

        if not file:
            return file

        # Maximum file size: 10 MB
        max_size = 10 * 1024 * 1024

        if file.size > max_size:
            raise forms.ValidationError(
                "File size cannot exceed 10 MB."
            )

        # Allowed file extensions and MIME types
        allowed_types = {
            ".pdf": "application/pdf",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".doc": "application/msword",
            ".docx": (
                "application/vnd.openxmlformats-officedocument."
                "wordprocessingml.document"
            ),
            ".txt": "text/plain",
        }

        file_name = file.name.lower()

        extension = None

        for allowed_extension in allowed_types:
            if file_name.endswith(allowed_extension):
                extension = allowed_extension
                break

        # Check file extension
        if extension is None:
            raise forms.ValidationError(
                "This file type is not allowed."
            )

        # Check MIME type
        content_type = getattr(
            file,
            "content_type",
            None,
        )

        expected_type = allowed_types[extension]

        if content_type and content_type != expected_type:
            raise forms.ValidationError(
                "The uploaded file type does not match "
                "its file extension."
            )

        # Validate actual image content
        if extension in {".jpg", ".jpeg", ".png"}:

            try:
                image = Image.open(file)
                image.verify()

            except Exception:
                raise forms.ValidationError(
                    "The uploaded file is not a valid image."
                )

            # Reset file pointer after verification
            file.seek(0)

        return file
