#!/usr/bin/env python3
"""
Setup Kaggle API for online dataset access (no download required)
"""
from kaggle.api.kaggle_api_extended import KaggleApi
import os
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / 'src'))
from config.kaggle_config import KaggleConfig

def setup_kaggle_api():
    """Initialize and authenticate Kaggle API"""
    
    print("Setting up Kaggle API for online access...")
    print("Note: Make sure KAGGLE_API_TOKEN is set in .env file")
    
    try:
        # Load secure configuration
        config = KaggleConfig()
        config.setup_environment()
        
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
        print("1. Ensure Kaggle API is installed: pip install kaggle python-dotenv")
        print("2. Copy .env.example to .env: cp .env.example .env")
        print("3. Add your token to .env file:")
        print("   KAGGLE_API_TOKEN=your_token_here")
        print("4. Or set environment variable:")
        print("   export KAGGLE_API_TOKEN=your_token_here")
        print("5. Accept dataset terms on Kaggle website")
        return False

if __name__ == "__main__":
    setup_kaggle_api()
