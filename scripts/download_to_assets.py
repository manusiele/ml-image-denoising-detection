#!/usr/bin/env python3
"""
Download Pascal VOC dataset to assets folder
"""
import os
import sys
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / 'src'))
from config.kaggle_config import KaggleConfig

def download_dataset():
    """Download Pascal VOC dataset to assets folder"""
    
    # Setup paths
    project_root = Path(__file__).parent.parent
    assets_dir = project_root / 'assets' / 'pascal-voc'
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    print("Configuring Kaggle API...")
    config = KaggleConfig()
    config.setup_environment()
    
    api = KaggleApi()
    api.authenticate()
    
    print(f"Downloading Pascal VOC dataset to {assets_dir}...")
    print("This will take 30-90 minutes depending on your connection.")
    
    # Download dataset
    api.dataset_download_files(
        'huanghanchina/pascal-voc-2012',
        path=str(assets_dir),
        unzip=True
    )
    
    print(f"Dataset downloaded successfully to {assets_dir}")
    
    # Verify download
    image_files = list(assets_dir.rglob('*.jpg'))
    print(f"Found {len(image_files)} images")
    
    return True

if __name__ == "__main__":
    try:
        download_dataset()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
