# Google Colab Setup Guide

Use Google Colab to run your project in the cloud with free GPU and storage!

## Why Use Colab?

✅ **Free cloud storage** - Dataset stays in the cloud  
✅ **Free GPU access** - Faster training  
✅ **No local storage needed** - Saves your disk space  
✅ **Pre-installed libraries** - Most packages already there  
✅ **Easy sharing** - Share notebooks with your team

## Quick Start

### Method 1: Direct Upload

1. **Go to Google Colab**: https://colab.research.google.com/

2. **Upload the setup notebook**:
   - Click "File" → "Upload notebook"
   - Upload `notebooks/00_colab_setup.ipynb`

3. **Run all cells**:
   - Click "Runtime" → "Run all"
   - Wait for dataset download (~5-10 minutes)

4. **Start working**:
   - Dataset is now in `/content/data/pascal-voc`
   - Run your other notebooks!

### Method 2: From GitHub

1. **Open Colab**: https://colab.research.google.com/

2. **Load from GitHub**:
   - Click "File" → "Open notebook"
   - Select "GitHub" tab
   - Enter: `manusiele/ml-image-denoising-detection`
   - Open `notebooks/00_colab_setup.ipynb`

3. **Run all cells**

## Storage Locations

### Colab Temporary Storage (Free, Fast)
- Location: `/content/data/`
- Size: Up to 100GB
- Lifetime: Session only (deleted when you close)
- **Best for**: Working on your project

### Google Drive (Persistent)
- Location: `/content/drive/MyDrive/`
- Size: 15GB free
- Lifetime: Permanent
- **Best for**: Saving results, models, reports

## Typical Workflow

```python
# 1. Download dataset to Colab storage (fast, temporary)
!kaggle datasets download -d huanghanchina/pascal-voc-2012 -p /content/data

# 2. Work with data in /content/data/
# ... your code here ...

# 3. Save results to Google Drive (permanent)
import shutil
shutil.copy('results.csv', '/content/drive/MyDrive/ml-project/')
```

## Tips

1. **Enable GPU**: Runtime → Change runtime type → GPU
2. **Keep session alive**: Run a cell every ~90 minutes
3. **Save frequently**: Copy important results to Google Drive
4. **Use checkpoints**: Save model checkpoints regularly

## Advantages Over Local

| Feature | Local | Colab |
|---------|-------|-------|
| Storage | Uses your disk | Cloud storage |
| GPU | Need to buy | Free! |
| Setup time | 30-90 min download | 5-10 min |
| Portability | One machine | Any browser |
| Collaboration | Hard | Easy sharing |

## Next Steps

After running `00_colab_setup.ipynb`:
1. Open `01_data_exploration.ipynb` in Colab
2. Update data paths to `/content/data/pascal-voc`
3. Continue with your project!
