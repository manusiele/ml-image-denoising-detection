# Object Detection and Recognition Using Convolutional Neural Networks on the Pascal VOC Dataset

A machine learning project implementing CNN-based object detection and recognition on the Pascal VOC dataset, with an integrated image denoising/enhancement stage to improve detection accuracy. Evaluation includes PSNR/SSIM for image quality and mAP for detection performance.

## 🚀 Quick Start (Google Colab - RECOMMENDED)

**Run in the cloud with free GPU - no local setup needed!**

1. Open Google Colab: https://colab.research.google.com/
2. Upload `notebooks/00_colab_setup.ipynb` OR
3. Use `notebooks/01_complete_pipeline.ipynb` for the full demo

**Advantages:**
- ✅ No local storage needed (dataset stays in cloud)
- ✅ Free GPU access
- ✅ Fast dataset download (5-10 minutes)
- ✅ Works from any browser

## 📁 Project Structure

```
ml-image-denoising-detection/
├── notebooks/              # Jupyter notebooks
│   ├── 00_colab_setup.ipynb       # Google Colab setup
│   ├── 01_complete_pipeline.ipynb # Complete working demo
│   ├── 02_image_denoising.ipynb   # Denoising techniques
│   └── 03_object_detection.ipynb  # Detection models
├── src/                    # Source code
│   ├── data/              # Data loaders (URL-based, no download)
│   ├── preprocessing/      # Image denoising/enhancement
│   ├── detection/          # Object detection models
│   └── evaluation/         # Metrics (PSNR, SSIM, mAP)
├── models/                 # Saved models
├── results/                # Output results and visualizations
└── requirements.txt        # Python dependencies
```

**Note**: No local dataset download required! Use SimpleImageLoader for quick testing or Google Colab for full dataset access.

## Setup Instructions

### Option 1: Google Colab (Recommended - No Setup!)

1. Go to https://colab.research.google.com/
2. Upload `notebooks/01_complete_pipeline.ipynb`
3. Run all cells - that's it!

### Option 2: Local Setup

1. Install dependencies:
```bash
pip install -r requirements-cpu.txt
```

2. Run Jupyter:
```bash
jupyter notebook notebooks/01_complete_pipeline.ipynb
```

**Security**: Your API token is stored in `.env` (git-ignored) and never committed to the repository. See [SECURITY.md](SECURITY.md) for details.

The project uses sample images from URLs for quick testing - no dataset download needed!

## Project Goals

1. **Object Detection**: Implement CNN-based object detection and recognition using Faster R-CNN
2. **Image Enhancement**: Apply denoising/restoration techniques to improve image quality
3. **Quality Evaluation**: Measure PSNR and SSIM metrics on enhanced images
4. **Performance Analysis**: Compare detection accuracy (mAP) on original vs. enhanced images
5. **Demonstrate**: How image preprocessing affects CNN detection performance
