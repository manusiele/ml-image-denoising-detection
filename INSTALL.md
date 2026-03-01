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

### Option 1: Install with increased timeout (recommended for slow connections)

```bash
pip install --upgrade pip
pip install --default-timeout=1000 -r requirements.txt
```

The `--default-timeout=1000` sets timeout to ~16 minutes (1000 seconds).

### Option 2: Install PyTorch separately first (for very slow connections)

PyTorch is the largest package (915 MB). Install it separately with extended timeout:

```bash
# Install PyTorch with 30-minute timeout
pip install --default-timeout=1800 torch torchvision

# Then install remaining packages
pip install -r requirements.txt
```

### Option 3: CPU-only PyTorch (smaller, faster download - 200MB vs 915MB)

```bash
# Install CPU-only version (much smaller)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Then install remaining packages
pip install -r requirements.txt
```

### Option 4: Install packages one by one (if connection keeps dropping)

```bash
pip install --default-timeout=1800 torch torchvision
pip install --default-timeout=600 kaggle python-dotenv
pip install --default-timeout=600 numpy pandas opencv-python
pip install --default-timeout=600 matplotlib seaborn
pip install --default-timeout=600 scikit-learn scikit-image scipy
pip install --default-timeout=600 jupyter ipykernel
pip install --default-timeout=600 pillow tqdm lxml
```

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
