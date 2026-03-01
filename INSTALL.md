# Installation Guide

## Step 1: Install Python Virtual Environment

```bash
sudo apt update
sudo apt install python3.12-venv
```

## Step 2: Create Virtual Environment

```bash
cd ml-image-denoising-detection
python3 -m venv venv
```

## Step 3: Activate Virtual Environment

```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

## Step 4: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install:
- PyTorch & TorchVision (deep learning)
- Kaggle API (dataset access)
- OpenCV & scikit-image (image processing)
- Jupyter (notebooks)
- And more...

## Step 5: Verify Setup

```bash
python scripts/download_dataset.py
```

You should see: "✓ Kaggle API authenticated successfully!"

## Step 6: Start Jupyter

```bash
jupyter notebook notebooks/
```

## Daily Usage

Every time you work on the project:

```bash
cd ml-image-denoising-detection
source venv/bin/activate  # Activate environment
jupyter notebook notebooks/  # Start working
```

To deactivate when done:
```bash
deactivate
```

## Troubleshooting

### If pip install fails:
```bash
# Try with --no-cache-dir
pip install --no-cache-dir -r requirements.txt
```

### If torch installation is slow:
```bash
# Install CPU-only version (faster, smaller)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### If you get permission errors:
Make sure you're in the virtual environment (you should see `(venv)` in prompt)
