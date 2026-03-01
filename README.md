# Hybrid Image Denoising and CNN-Based Object Detection

A machine learning project implementing image denoising with quality evaluation (PSNR/SSIM) followed by CNN-based object detection on the Pascal VOC dataset.

## Project Structure

```
ml-image-denoising-detection/
├── data/                    # Dataset directory (auto-created)
│   └── pascal-voc/         # Pascal VOC dataset
├── notebooks/              # Jupyter notebooks
├── src/                    # Source code
│   ├── preprocessing/      # Image denoising/enhancement
│   ├── detection/          # Object detection models
│   └── evaluation/         # Metrics (PSNR, SSIM, mAP)
├── models/                 # Saved models
├── results/                # Output results and visualizations
└── requirements.txt        # Python dependencies
```

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure Kaggle API:
```bash
# Place your kaggle.json in ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

3. Download Pascal VOC dataset:
```bash
python scripts/download_dataset.py
```

## Project Goals

1. **Image Preprocessing**: Apply denoising/enhancement techniques
2. **Quality Evaluation**: Measure PSNR and SSIM metrics
3. **Object Detection**: Train/evaluate CNN-based detector
4. **Impact Analysis**: Compare detection performance (mAP) on original vs. enhanced images
