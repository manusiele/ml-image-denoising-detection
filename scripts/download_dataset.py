#!/usr/bin/env python3
"""
Download Pascal VOC dataset using Kaggle API
"""
import os
import subprocess
import zipfile
from pathlib import Path

def download_pascal_voc():
    """Download Pascal VOC dataset from Kaggle"""
    
    # Create data directory
    data_dir = Path("data/pascal-voc")
    data_dir.mkdir(parents=True, exist_ok=True)
    
    print("Downloading Pascal VOC dataset from Kaggle...")
    print("Note: Make sure you have kaggle.json configured in ~/.kaggle/")
    
    try:
        # Download using Kaggle API
        # Pascal VOC 2012 dataset
        subprocess.run([
            "kaggle", "datasets", "download", 
            "-d", "huanghanchina/pascal-voc-2012",
            "-p", str(data_dir),
            "--unzip"
        ], check=True)
        
        print(f"\n✓ Dataset downloaded successfully to {data_dir}")
        print("\nDataset structure:")
        for item in data_dir.rglob("*"):
            if item.is_dir():
                print(f"  📁 {item.relative_to(data_dir)}")
        
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error downloading dataset: {e}")
        print("\nTroubleshooting:")
        print("1. Ensure Kaggle API is installed: pip install kaggle")
        print("2. Download kaggle.json from https://www.kaggle.com/settings")
        print("3. Place it in ~/.kaggle/ and run: chmod 600 ~/.kaggle/kaggle.json")
        print("4. Accept dataset terms on Kaggle website")
        return False
    
    return True

if __name__ == "__main__":
    download_pascal_voc()
