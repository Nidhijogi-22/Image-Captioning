"""
BLIP Image Captioning Model.

Responsible for:
- Loading the BLIP processor
- Loading the BLIP model
- Selecting CPU/GPU
- Generating captions
"""

import logging

import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

from models.model_config import (
    MODEL_NAME,
    MAX_NEW_TOKENS,
    NUM_BEAMS,
    USE_GPU,
)


logger = logging.getLogger(__name__)


class ImageCaptioningModel:
    """
    Wrapper around the BLIP image captioning model.
    """

    def __init__(self):
        """
        Initialize processor, model and device.
        """

        self.device = self._get_device()

        logger.info(
            "Loading image captioning model: %s",
            MODEL_NAME
        )

        self.processor = BlipProcessor.from_pretrained(
            MODEL_NAME
        )

        self.model = BlipForConditionalGeneration.from_pretrained(
            MODEL_NAME
        )

        self.model.to(self.device)

        # Evaluation mode
        self.model.eval()

        logger.info(
            "Model loaded successfully on %s",
            self.device
        )

    @staticmethod
    def _get_device():
        """
        Select GPU if available, otherwise CPU.
        """

        if USE_GPU and torch.cuda.is_available():
            return torch.device("cuda")

        return torch.device("cpu")

    def generate_caption(self, image: Image.Image) -> str:
        """
        Generate a caption for the supplied PIL image.

        Args:
            image: PIL Image

        Returns:
            Generated caption as string.
        """

        if image is None:
            raise ValueError("Image cannot be None.")

        if not isinstance(image, Image.Image):
            raise TypeError(
                "Input must be a PIL.Image.Image object."
            )

        # BLIP works with RGB images
        image = image.convert("RGB")

        # Process image
        inputs = self.processor(
            images=image,
            return_tensors="pt"
        )

        # Move tensors to selected device
        inputs = {
            key: value.to(self.device)
            for key, value in inputs.items()
        }

        # Generate caption
        with torch.no_grad():
            output = self.model.generate(
                **inputs,
                max_new_tokens=MAX_NEW_TOKENS,
                num_beams=NUM_BEAMS,
                early_stopping=True
            )

        # Decode generated tokens
        caption = self.processor.decode(
            output[0],
            skip_special_tokens=True
        )

        caption = caption.strip()

        logger.info(
            "Caption generated successfully."
        )

        return caption