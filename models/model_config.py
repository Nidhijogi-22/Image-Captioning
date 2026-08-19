"""
Configuration for the image captioning model.
"""

MODEL_NAME = "Salesforce/blip-image-captioning-base"

# Generation parameters
MAX_NEW_TOKENS = 50
NUM_BEAMS = 5

# Device
USE_GPU = True