import os
import cv2
from ultralytics import YOLO
from PIL import Image as PILImage
from src.jogo.visao_computacional.camera import Captura

class ImagePredictor:
    def __init__(self):
        self.model_path = 'src/jogo/visao_computacional/best.pt'
        self.model = YOLO(self.model_path)
        self.path = 'src/jogo/visao_computacional/predict/FotoTabuleiro.png'
    
    def capture_image(self):
        foto = Captura()
        foto.connect()
        foto.capCamera()
    
    def predict_image(self, conf=0.25, save=True, save_txt=True):
        results = self.model.predict(source=self.path, conf=conf, save=save, save_txt=save_txt, project='src/jogo/visao_computacional',name='predict',exist_ok=True)
        # results[0].tojson()
        return results

#Testes:
# foto = ImagePredictor()
# foto.capture_image()
# foto.predict_image()