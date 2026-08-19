# 🖼️ AI Image Captioning System

An AI-powered image captioning application that generates natural-language descriptions of images.

The system supports both image uploads and camera capture.

---

## Features

- Upload an image
- Capture an image using camera
- AI-based image caption generation
- BLIP pretrained vision-language model
- Image validation
- Image preprocessing
- Caption cleaning
- Caption validation
- Caption quality indicator
- Caption history
- Download generated caption
- GPU acceleration when available
- Logging
- Unit testing

---

## Technology Stack

- Python
- Streamlit
- PyTorch
- Transformers
- BLIP
- Pillow

---

## Project Architecture

User
    ↓
Streamlit UI
    ↓
Image Service
    ↓
Image Validation
    ↓
Caption Service
    ↓
BLIP Model
    ↓
Caption
    ↓
Result UI

---

## Team Structure

### Member 1 - ML Developer

Responsible for:

- BLIP model
- Model configuration
- Caption generation
- Model testing

Files:

models/

---

### Member 2 - Backend Developer

Responsible for:

- Image validation
- Image preprocessing
- Caption service
- Logging
- Backend testing

Files:

services/
utils/

---

### Member 3 - UI Developer

Responsible for:

- Streamlit application
- Upload interface
- Camera interface
- Result display

Files:

app.py
ui/

---

## Installation

Create a virtual environment.

### Windows

```bash
python -m venv venv