"""
Para usar esse arquivo em primeiro lugar você tem que se atentar a que tipo de formato do arquivo você vai querer dessa
forma tera que modificar o doc_name na 11 linha do código percebão que o formato está ??? troquem sé não vai da erro,
além disso, tem que ter certeza que o seu ambiente conda terá instalado o rria-api, depois basta apenas você dizer o
nome daquela posição e apertar enter para gravar a posição dentro do arquivo e printar a mesma no terminal
"""

from rria_api.robot_enum import RobotEnum
from rria_api.robot_object import RobotObject

doc_name = 'positions_kinova1.txt'

robot = RobotObject('192.168.2.10', RobotEnum.GEN3_LITE)
robot.connect_robot()

conditions = True

try:
    doc_file_ = open(doc_name)
    doc_file_.close()

except FileNotFoundError:
    with open(doc_name, 'a+') as doc_file:
        doc_file.write('Position\tType\tJoints\n')

while conditions:
    choice = input("Digite o nome da posição ou Q(q) para sair do programa:\n")

    if choice == "q" or choice == "Q":
        conditions = False

    else:
        joint_position = robot.get_joints()
        cartesian_position = robot.get_cartesian()

        print(joint_position)
        print(cartesian_position)

        with open(doc_name, 'a+') as doc_file:

            doc_file.write(f'{choice}\tjoints\t{joint_position}\n')
            doc_file.write(f"{choice}\tcartesian\t{cartesian_position}\n")