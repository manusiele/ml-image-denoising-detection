# Object Detection and Recognition Using CNNs on Pascal VOC Dataset

CNN-based object detection with image denoising preprocessing. Evaluates PSNR/SSIM for image quality and detection performance comparison.

## Quick Start

### Google Colab (Recommended)

1. Open https://colab.research.google.com/
2. Upload `notebooks/00_colab_setup.ipynb`
3. Run all cells
4. Upload your own images using the upload cell

### Local Setup

1. Install dependencies:
```bash
pip install -r requirements-cpu.txt
```

2. Download dataset:
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
├── assets/                 # Local dataset storage
├── notebooks/
│   ├── 00_colab_setup.ipynb       # Colab complete pipeline
│   ├── 01_complete_pipeline.ipynb # URL-based demo
│   ├── 02_local_pipeline.ipynb    # Local assets demo
│   └── 03_upload_and_process.ipynb # Custom image upload
├── src/
│   ├── data/local_loader.py       # Local data loader
│   ├── preprocessing/denoising.py # Denoising techniques
│   ├── detection/model.py         # Detection model
│   └── evaluation/metrics.py      # PSNR/SSIM/mAP metrics
├── scripts/download_to_assets.py  # Dataset downloader
└── requirements-cpu.txt           # Dependencies
```

## Features

1. Image denoising (Gaussian, Bilateral, Non-Local Means)
2. Quality metrics (PSNR, SSIM)
3. Object detection (Faster R-CNN)
4. Performance comparison
5. Custom image upload support

## Results

- PSNR improvement: 25-32 dB
- Detection accuracy maintained on denoised images
- Reduced false positives with proper thresholding
