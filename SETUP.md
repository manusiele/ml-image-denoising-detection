# Setup Guide

## 1. Install Dependencies

```bash
cd ml-image-denoising-detection
pip install -r requirements.txt
```

## 2. Configure Kaggle API

### Get your API credentials:
1. Go to https://www.kaggle.com/settings
2. Scroll to "API" section
3. Click "Create New API Token"
4. Download `kaggle.json`

### Setup credentials:
```bash
# Create kaggle directory
mkdir -p ~/.kaggle

# Move your kaggle.json there
mv ~/Downloads/kaggle.json ~/.kaggle/

# Set permissions
chmod 600 ~/.kaggle/kaggle.json
```

## 3. Setup Kaggle API (No Download Required!)

```bash
python scripts/download_dataset.py
```

This will authenticate your Kaggle API for online access. The dataset stays on Kaggle - we access it directly via API!

## 4. Start Working

Open Jupyter notebooks:
```bash
jupyter notebook notebooks/
```

Start with:
1. `01_data_exploration.ipynb` - Explore the dataset
2. `02_image_denoising.ipynb` - Apply denoising and measure PSNR/SSIM
3. `03_object_detection.ipynb` - Train detector and compare mAP

## Project Workflow

1. **Data Access**: Connect to Pascal VOC via Kaggle API (no download!)
2. **Data Exploration**: Stream and explore images online
3. **Image Preprocessing**: Apply denoising techniques (Gaussian, Bilateral, NLM)
4. **Quality Evaluation**: Measure PSNR and SSIM on denoised images
5. **Object Detection**: Train CNN detector (Faster R-CNN)
6. **Impact Analysis**: Compare mAP on original vs. denoised images
7. **Report**: Document findings showing how denoising affects detection

## Expected Outcomes

- PSNR values: 20-50 dB (higher is better)
- SSIM values: 0.7-1.0 (closer to 1 is better)
- mAP comparison showing detection improvement on enhanced images
