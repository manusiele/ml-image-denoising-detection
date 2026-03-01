# Object Detection and Recognition Using CNNs on Pascal VOC Dataset

CNN-based object detection with image denoising preprocessing. Evaluates PSNR/SSIM for image quality and mAP for detection performance.

## Quick Start

### Option 1: Google Colab (Recommended)

1. Open https://colab.research.google.com/
2. Upload `notebooks/00_colab_setup.ipynb`
3. Run all cells

### Option 2: Local Setup

1. Install dependencies:
```bash
pip install -r requirements-cpu.txt
```

2. Download dataset to assets folder:
```bash
python scripts/download_to_assets.py
```

3. Run notebook:
```bash
jupyter notebook notebooks/02_local_pipeline.ipynb
```

## Project Structure

```
ml-image-denoising-detection/
├── assets/                 # Dataset storage (local only)
├── notebooks/              # Jupyter notebooks
│   ├── 00_colab_setup.ipynb       # Colab setup
│   ├── 01_complete_pipeline.ipynb # URL-based demo
│   └── 02_local_pipeline.ipynb    # Local assets demo
├── src/                    # Source code
│   ├── data/              # Data loaders
│   ├── preprocessing/      # Image denoising
│   ├── detection/          # Object detection
│   └── evaluation/         # Metrics (PSNR, SSIM, mAP)
├── scripts/               # Utility scripts
└── requirements-cpu.txt   # Dependencies
```

## Project Goals

1. Image denoising with multiple techniques
2. Quality evaluation using PSNR and SSIM
3. CNN-based object detection (Faster R-CNN)
4. Performance comparison on original vs enhanced images
