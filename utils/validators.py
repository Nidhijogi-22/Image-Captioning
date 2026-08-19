"""
Validation functions for uploaded/captured images.
"""

from io import BytesIO

from PIL import Image, UnidentifiedImageError


ALLOWED_FORMATS = {
    "JPEG",
    "PNG",
    "WEBP",
    "JPG"
}

MAX_FILE_SIZE_MB = 10


def validate_uploaded_image(uploaded_file):
    """
    Validate a Streamlit uploaded file.

    Returns:
        tuple: (is_valid, message)
    """

    if uploaded_file is None:
        return False, "No image was provided."

    # Check file size
    if hasattr(uploaded_file, "size"):

        max_size = MAX_FILE_SIZE_MB * 1024 * 1024

        if uploaded_file.size > max_size:
            return (
                False,
                f"Image size must be below "
                f"{MAX_FILE_SIZE_MB} MB."
            )

    try:

        image_bytes = uploaded_file.getvalue()

        image = Image.open(
            BytesIO(image_bytes)
        )

        image.verify()

        # Open again after verify
        image = Image.open(
            BytesIO(image_bytes)
        )

        image_format = image.format

        if image_format not in ALLOWED_FORMATS:
            return (
                False,
                f"Unsupported image format: {image_format}"
            )

        if image.width < 32 or image.height < 32:
            return (
                False,
                "Image resolution is too small."
            )

        return True, "Valid image."

    except (UnidentifiedImageError, OSError):

        return (
            False,
            "The uploaded file is not a valid image."
        )


def validate_pil_image(image):
    """
    Validate a PIL image.
    """

    if image is None:
        return False, "No image provided."

    if not isinstance(image, Image.Image):
        return False, "Invalid image object."

    if image.width < 32 or image.height < 32:
        return False, "Image resolution is too small."

    return True, "Valid image."