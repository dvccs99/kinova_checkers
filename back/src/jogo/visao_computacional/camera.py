import cv2

class Captura:
    def __init__(self):
        self.camera = None

    def connect(self):
        self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def disconnect(self):
        self.camera.release()

    def capCamera(self):
        frame = None
        width = 640
        height = 640

        if self.camera.isOpened():
            validacao, frame = self.camera.read()
            if validacao:
                resized_image = cv2.resize(frame, (width, height))
                cv2.imwrite("src/jogo/visao_computacional/predict/FotoTabuleiro.png", resized_image)
            
        self.camera.release()
        cv2.destroyAllWindows()

        return frame



