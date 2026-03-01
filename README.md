# Object Detection and Recognition Using Convolutional Neural Networks on the Pascal VOC Dataset

A machine learning project implementing CNN-based object detection and recognition on the Pascal VOC dataset, with an integrated image denoising/enhancement stage to improve detection accuracy. Evaluation includes PSNR/SSIM for image quality and mAP for detection performance.

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

3. Setup Kaggle API (no download needed!):
```bash
python scripts/download_dataset.py
```

The project uses Kaggle's API to access Pascal VOC dataset online - no local download required!

## Project Goals

1. **Object Detection**: Implement CNN-based object detection and recognition using Faster R-CNN
2. **Image Enhancement**: Apply denoising/restoration techniques to improve image quality
3. **Quality Evaluation**: Measure PSNR and SSIM metrics on enhanced images
4. **Performance Analysis**: Compare detection accuracy (mAP) on original vs. enhanced images
5. **Demonstrate**: How image preprocessing affects CNN detection performance
