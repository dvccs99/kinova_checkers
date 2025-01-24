from flask import Flask, request, jsonify
from jogo.tabuleiro import Tabuleiro
import os
from src.camera import Captura
from src.real_robot import RealRobot

app = Flask(__name__)

camera = Captura()

tabuleiro = Tabuleiro()

robot = RealRobot(num_int=1)  # caso erro mudar esse valor aqui num_int 

@app.route('/connect', methods=['POST'])
def connect():
    try:
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
        robot.desconectar()
        return jsonify({"message": "Robô desconectado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/board', methods=['GET'])
def get_board():
    board_representation = {pos: peca for pos, peca in tabuleiro.posicoes.items()}
    return jsonify({'board': board_representation}), 200

# mover a peça sem o robo
@app.route('/move', methods=['POST'])
def move():
    data = request.json
    inicio = data.get('inicio')
    fim = data.get('fim')
    tabuleiro.mover_peca(inicio, fim)
    return jsonify({'message': f'Peça movida de {inicio} para {fim}'}), 200

@app.route('/remove_piece', methods=['POST'])
def remove_piece():
    try:
        data = request.json
        posicao_TB = data['posicao_TB']
        robot.remover_peca(posicao_TB)
        return jsonify({"message": f"Peça removida da posição {posicao_TB} com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/move_piece', methods=['POST'])
def move_piece():
    try:
        data = request.json
        posicao_peca = data['posicao_peca']
        array_caminho = data['array_caminho']
        robot.mov_caminho(posicao_peca, array_caminho)
        return jsonify({"message": "Peça movida com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/capture', methods=['POST'])
def capture():
    try:
        # Caminho onde a imagem será salva
        save_path = 'foto_tabuleiro.jpg'
        success = camera.capCamera(save_path)

        if success:
            return jsonify({"message": "Imagem capturada com sucesso!", "image_path": save_path}), 200
        else:
            return jsonify({"error": "Erro ao capturar imagem"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
