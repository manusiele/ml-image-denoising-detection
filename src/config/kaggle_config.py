"""
Secure Kaggle API configuration
"""
import os
from pathlib import Path
from dotenv import load_dotenv

class KaggleConfig:
    """Secure Kaggle API configuration manager"""
    
    def __init__(self):
        """Initialize configuration"""
        # Load environment variables from .env file
        env_path = Path(__file__).parent.parent.parent / '.env'
        load_dotenv(env_path)
        
        self.api_token = None
        self._load_token()
    
    def _load_token(self):
        """Load API token from environment variable"""
        self.api_token = os.getenv('KAGGLE_API_TOKEN')
        
        if not self.api_token:
            raise ValueError(
                "KAGGLE_API_TOKEN not found!\n"
                "Please set it in .env file or as environment variable:\n"
                "export KAGGLE_API_TOKEN=your_token_here"
            )
    
    def setup_environment(self):
        """Setup Kaggle environment variables"""
        if self.api_token:
            os.environ['KAGGLE_API_TOKEN'] = self.api_token
            return True
        return False
    
    @staticmethod
    def is_configured():
        """Check if Kaggle API is configured"""
        return 'KAGGLE_API_TOKEN' in os.environ or os.getenv('KAGGLE_API_TOKEN') is not None
