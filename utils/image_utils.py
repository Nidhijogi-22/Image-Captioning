"""
Image processing utilities.
"""

from io import BytesIO

from PIL import Image, ImageOps


def bytes_to_image(image_bytes):
    """
    Convert image bytes into a PIL Image.
    """

    image = Image.open(
        BytesIO(image_bytes)
    )

    image = ImageOps.exif_transpose(
        image
    )

    return image.convert("RGB")


def uploaded_file_to_image(uploaded_file):
    """
    Convert Streamlit UploadedFile to PIL image.
    """

    image_bytes = uploaded_file.getvalue()

    return bytes_to_image(
        image_bytes
    )


def prepare_image(image):
    """
    Prepare an image for the captioning model.

    Converts image to RGB and handles EXIF orientation.
    """

    if image is None:
        raise ValueError(
            "Cannot prepare a None image."
        )

    image = ImageOps.exif_transpose(
        image
    )

    return image.convert("RGB")