"""
Evaluation metrics: PSNR, SSIM, and mAP
"""
import numpy as np
import cv2
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

class ImageQualityMetrics:
    """Calculate image quality metrics"""
    
    @staticmethod
    def calculate_psnr(original, processed):
        """
        Calculate Peak Signal-to-Noise Ratio (PSNR)
        Higher is better (typically 20-50 dB)
        """
        return peak_signal_noise_ratio(original, processed)
    
    @staticmethod
    def calculate_ssim(original, processed):
        """
        Calculate Structural Similarity Index (SSIM)
        Range: [-1, 1], where 1 means identical images
        """
        # Convert to grayscale if needed
        if len(original.shape) == 3:
            original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
            processed_gray = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
        else:
            original_gray = original
            processed_gray = processed
        
        return structural_similarity(original_gray, processed_gray)
    
    @staticmethod
    def evaluate_image_pair(original, processed):
        """Evaluate both PSNR and SSIM"""
        psnr = ImageQualityMetrics.calculate_psnr(original, processed)
        ssim = ImageQualityMetrics.calculate_ssim(original, processed)
        
        return {
            'psnr': psnr,
            'ssim': ssim
        }


class DetectionMetrics:
    """Calculate object detection metrics (mAP)"""
    
    @staticmethod
    def calculate_iou(box1, box2):
        """Calculate Intersection over Union"""
        x1 = max(box1[0], box2[0])
        y1 = max(box1[1], box2[1])
        x2 = min(box1[2], box2[2])
        y2 = min(box1[3], box2[3])
        
        intersection = max(0, x2 - x1) * max(0, y2 - y1)
        area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
        area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
        union = area1 + area2 - intersection
        
        return intersection / union if union > 0 else 0
    
    @staticmethod
    def calculate_map(predictions, ground_truths, iou_threshold=0.5):
        """
        Calculate mean Average Precision (mAP)
        Simplified version for demonstration
        """
        # Implementation would depend on your detection model output format
        # This is a placeholder structure
        pass
