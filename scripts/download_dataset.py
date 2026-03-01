#!/usr/bin/env python3
"""
Setup Kaggle API for online dataset access (no download required)
"""
from kaggle.api.kaggle_api_extended import KaggleApi
import os

def setup_kaggle_api():
    """Initialize and authenticate Kaggle API"""
    
    print("Setting up Kaggle API for online access...")
    print("Note: Make sure you have kaggle.json configured in ~/.kaggle/")
    
    try:
        api = KaggleApi()
        api.authenticate()
        
        print("\n✓ Kaggle API authenticated successfully!")
        print("\nYou can now access Pascal VOC dataset online without downloading.")
        print("\nAvailable Pascal VOC datasets:")
        
        # List available Pascal VOC datasets
        datasets = api.dataset_list(search='pascal voc')
        for i, dataset in enumerate(datasets[:5], 1):
            print(f"{i}. {dataset.ref} - {dataset.title}")
        
        print("\n✓ Setup complete! Use the API in your notebooks.")
        return True
        
    except Exception as e:
        print(f"\n✗ Error setting up Kaggle API: {e}")
        print("\nTroubleshooting:")
        print("1. Ensure Kaggle API is installed: pip install kaggle")
        print("2. Download kaggle.json from https://www.kaggle.com/settings")
        print("3. Place it in ~/.kaggle/ and run: chmod 600 ~/.kaggle/kaggle.json")
        print("4. Accept dataset terms on Kaggle website")
        return False

if __name__ == "__main__":
    setup_kaggle_api()
