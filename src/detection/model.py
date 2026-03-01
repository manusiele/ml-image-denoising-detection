"""
CNN-based object detection model
"""
import torch
import torch.nn as nn
import torchvision
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

class ObjectDetector:
    """Wrapper for object detection model"""
    
    def __init__(self, num_classes=21, pretrained=True):
        """
        Initialize object detector
        Args:
            num_classes: Number of classes (20 VOC classes + background)
            pretrained: Use pretrained weights
        """
        self.num_classes = num_classes
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = self._build_model(pretrained)
        
    def _build_model(self, pretrained):
        """Build Faster R-CNN model"""
        # Load pretrained model
        model = fasterrcnn_resnet50_fpn(pretrained=pretrained)
        
        # Replace the classifier head
        in_features = model.roi_heads.box_predictor.cls_score.in_features
        model.roi_heads.box_predictor = FastRCNNPredictor(in_features, self.num_classes)
        
        model.to(self.device)
        return model
    
    def train_model(self, train_loader, num_epochs=10, lr=0.005):
        """Train the detection model"""
        self.model.train()
        optimizer = torch.optim.SGD(
            self.model.parameters(),
            lr=lr,
            momentum=0.9,
            weight_decay=0.0005
        )
        
        for epoch in range(num_epochs):
            epoch_loss = 0
            for images, targets in train_loader:
                images = [img.to(self.device) for img in images]
                targets = [{k: v.to(self.device) for k, v in t.items()} for t in targets]
                
                loss_dict = self.model(images, targets)
                losses = sum(loss for loss in loss_dict.values())
                
                optimizer.zero_grad()
                losses.backward()
                optimizer.step()
                
                epoch_loss += losses.item()
            
            print(f"Epoch {epoch+1}/{num_epochs}, Loss: {epoch_loss:.4f}")
    
    def evaluate(self, test_loader):
        """Evaluate model on test set"""
        self.model.eval()
        predictions = []
        
        with torch.no_grad():
            for images, targets in test_loader:
                images = [img.to(self.device) for img in images]
                outputs = self.model(images)
                predictions.extend(outputs)
        
        return predictions
    
    def save_model(self, path):
        """Save model weights"""
        torch.save(self.model.state_dict(), path)
    
    def load_model(self, path):
        """Load model weights"""
        self.model.load_state_dict(torch.load(path, map_location=self.device))
