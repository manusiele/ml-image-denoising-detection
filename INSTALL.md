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

### RECOMMENDED: CPU-Only Installation (for non-NVIDIA systems)

Since you don't have NVIDIA GPU, use CPU-only versions (much smaller and faster):

```bash
pip install --upgrade pip

# Install PyTorch CPU-only (200MB instead of 915MB)
pip install --default-timeout=1800 torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Install remaining packages
pip install --default-timeout=1800 -r requirements-cpu.txt
```

### Option 1: Install with increased timeout (if using GPU version)

```bash
pip install --upgrade pip
pip install --default-timeout=1800 -r requirements.txt
```

The `--default-timeout=1800` sets timeout to 30 minutes.

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

### Network timeout during installation:
```bash
# Increase timeout to 30 minutes
pip install --default-timeout=1800 -r requirements.txt

# Or install CPU-only PyTorch (much smaller - 200MB vs 915MB)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```

### If pip install fails:
```bash
# Try with --no-cache-dir
pip install --no-cache-dir --default-timeout=1800 -r requirements.txt
```

### If connection keeps dropping:
```bash
# Install packages individually with retries
pip install --default-timeout=1800 --retries 10 torch torchvision
```

### Check your internet connection:
```bash
# Test download speed
curl -o /dev/null http://speedtest.wdc01.softlayer.com/downloads/test10.zip

# If connection is unstable, use CPU-only PyTorch (recommended)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```
