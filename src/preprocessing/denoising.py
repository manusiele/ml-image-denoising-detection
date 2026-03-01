"""
Image denoising and enhancement techniques
"""
import cv2
import numpy as np
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_float, img_as_ubyte

class ImageDenoiser:
    """Apply various denoising techniques to images"""
    
    @staticmethod
    def gaussian_blur(image, kernel_size=(5, 5)):
        """Apply Gaussian blur denoising"""
        return cv2.GaussianBlur(image, kernel_size, 0)
    
    @staticmethod
    def bilateral_filter(image, d=9, sigma_color=75, sigma_space=75):
        """Apply bilateral filtering (edge-preserving)"""
        return cv2.bilateralFilter(image, d, sigma_color, sigma_space)
    
    @staticmethod
    def non_local_means(image, h=10, template_window_size=7, search_window_size=21):
        """Apply Non-Local Means denoising"""
        return cv2.fastNlMeansDenoisingColored(
            image, None, h, h, template_window_size, search_window_size
        )
    
    @staticmethod
    def median_filter(image, kernel_size=5):
        """Apply median filtering"""
        return cv2.medianBlur(image, kernel_size)
    
    @staticmethod
    def morphological_opening(image, kernel_size=(5, 5)):
        """Apply morphological opening"""
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    
    @staticmethod
    def adaptive_histogram_equalization(image):
        """Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)"""
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        l = clahe.apply(l)
        enhanced = cv2.merge([l, a, b])
        return cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
