from flask import Flask, request, jsonify
from jogo.tabuleiro import Tabuleiro
import os
from visao_computacional.camera import Captura
from robo.real_robot import RealRobot
from jogo.mapeamento import Mapeamento

app = Flask(__name__)

camera = Captura()

tabuleiro = Tabuleiro()

@app.route('/connect', methods=['POST'])
def connect():
    try:
        data = request.json
        qual_robo = data['qual_robo']
        if qual_robo == 1:
            robot = RealRobot(qual_robo=1) 
            robot.conectar()
            pos = robot.robot.get_cartesian()
            robot.fechar_garra(1.3)
            robot.robot.move_cartesian(*pos)    
        elif qual_robo == 2:
            robot = RealRobot(qual_robo=2) 
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
        robot = RealRobot() 
        robot.desconectar()
        return jsonify({"message": "Robô desconectado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/board', methods=['GET'])
def get_board():
    board_representation = {pos: peca for pos, peca in tabuleiro.posicoes.items()}
    return jsonify({'board': board_representation}), 200

@app.route('/remove_piece', methods=['POST'])
def remove_piece():
    try:
        data = request.json
        qual_robo = data['qual_robo']
        if qual_robo == 1:
            robot = RealRobot(num_int=1) 
            data = request.json
            posicao_TB = data['posicao_TB']
            robot.remover_peca(posicao_TB)
        elif qual_robo == 2:
            robot = RealRobot(num_int=2) 
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
        qual_robo = data['qual_robo']
        if qual_robo == 1:
            robot = RealRobot(num_int=1) 
            data = request.json
            posicao_peca = data['posicao_peca']
            array_caminho = data['array_caminho']
            robot.mov_caminho(posicao_peca, array_caminho)
        elif qual_robo == 2:
            robot = RealRobot(num_int=2) 
            data = request.json
            posicao_peca = data['posicao_peca']
            array_caminho = data['array_caminho']
            robot.mov_caminho(posicao_peca, array_caminho)
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