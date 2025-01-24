from flask import Flask, request, jsonify
from jogo.tabuleiro import Tabuleiro
import os
from visao_computacional.camera import Captura
from robo.real_robot import RealRobot
from jogo.mapeamento import Mapeamento
from visao_computacional.tradutor_tabuleiro import PosicaoTabuleiro
from ultralytics import YOLO
from PIL import Image as PILImage

app = Flask(__name__)

camera = Captura()
tabuleiro = Tabuleiro()

# importante daqui 

# conecta o robo e apresenta o bord sem o posicaoTbauleiro
@app.route('/board1', methods=['GET'])
def get_board():
    try:
        robot = RealRobot(num_int=1) 
        robot.conectar() 
        board_representation = {pos: peca for pos, peca in tabuleiro.posicoes.items()}
        return jsonify({'board': board_representation}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# retorna a posicao do tabuleiro apenas    
@app.route('/board2', methods=['GET'])
def get_board():
    num_robot = request.args.get('num_robot', default=1, type=int)
    arquivo = request.args.get('arquivo', default='./runs/detect/predict/labels/FotoTabuleiro', type=str)
    
    posicao_tabuleiro = PosicaoTabuleiro(num_robot)
    resultado = PosicaoTabuleiro.lerArquivo(arquivo, posicao_tabuleiro)
    
    return jsonify(resultado)

# conecta e retonra a posicao do tabuleiro
@app.route('/board3', methods=['GET'])
def get_board():
    try:
        robot = RealRobot(num_int=1) 
        robot.conectar() 
        
        num_robot = request.args.get('num_robot', default=1, type=int)
        arquivo = request.args.get('arquivo', default='./runs/detect/predict/labels/FotoTabuleiro', type=str)
        
        posicao_tabuleiro = PosicaoTabuleiro(num_robot)
        resultado = PosicaoTabuleiro.lerArquivo(arquivo, posicao_tabuleiro)
        
        return jsonify({resultado}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# tentativa maior de conectar tudo
@app.route('/board', methods=['GET'])
def process_board():
    try:
        robot = RealRobot(num_int=1) 
        robot.conectar() 
        
        captura = Captura()
        captura.capCamera()
        
        model_path = 'src/runs/detect/train3/weights/best.pt'
        model = YOLO(model_path)

        input_image_path = 'src/image/FotoTabuleiro.png'
        results = model.predict(source=input_image_path, conf=0.25, save=True, save_txt=True)
        output_image_path = './runs/detect/predict/FotoTabuleiro.png'

        prediction_image = PILImage.open(output_image_path)
        prediction_image.show()

        posicao_tabuleiro = PosicaoTabuleiro(num_robot=1)
        resultado = posicao_tabuleiro.lerArquivo('./runs/detect/predict/labels/FotoTabuleiro')
        
        return jsonify({resultado}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ate aqui

@app.route('/connect', methods=['POST'])
def connect():
    try:
        robot = RealRobot(num_int=1) 
        robot.conectar()
        pos = robot.robot.get_cartesian()
        robot.fechar_garra(1.3)
        robot.robot.move_cartesian(*pos)
        return jsonify({"message": "Robô conectado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/disconnect', methods=['POST'])
def disconnect():
    try:
        robot = RealRobot(num_int=1) 
        robot.desconectar()
        return jsonify({"message": "Robô desconectado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/remove_piece', methods=['POST'])
def remove_piece():
    try:
        data = request.json
        posicao_TB = data['posicao_TB']
        robot = RealRobot(num_int=1)
        robot.conectar()
        robot.remover_peca(posicao_TB)
        robot.desconectar()
        return jsonify({"message": f"Peça removida da posição {posicao_TB} com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/move_piece', methods=['POST'])
def move_piece():
    try:
        data = request.json
        posicao_peca = data['posicao_peca']
        array_caminho = data['array_caminho']
        robot = RealRobot(num_int=1)
        robot.conectar()
        robot.mov_caminho(posicao_peca, array_caminho)
        robot.desconectar()
        return jsonify({"message": "Peça movida com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/detect', methods=['POST'])
def detect():
    try:
        mapeamento = Mapeamento()
        success = camera.capCamera()
        tabuleiro_posicoes = mapeamento.detectar_Pecas(success)
        
        if tabuleiro_posicoes:
            return jsonify({"message": "Detecção concluída com sucesso!", "tabuleiro": tabuleiro_posicoes}), 200
        else:
            return jsonify({"error": "Erro ao capturar imagem"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
