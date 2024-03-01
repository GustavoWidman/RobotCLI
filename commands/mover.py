from classes.robot import RobotWrapper
from enum import Enum
from typing_extensions import Annotated
from utils.text import printc, cstring
# import inquirer
import yaspin
import typer


app = typer.Typer()

class Pos(str, Enum):
	x = "x"
	y = "y"
	z = "z"

@app.command(short_help="Move o robô para uma posição específica.")
def mover(posição: Pos, valor: Annotated[float, typer.Option(prompt=True)]):
	"""
		Move o robô para uma posição específica

			- posicao: A posição que o robô deve se mover (x, y ou z)

			- valor: O valor que a posição deve ter

		Exemplo:

			$ python main.py mover x

			$ Valor: 100

			Isso adiciona 100 à posição X do robô (mantendo as posições Y e Z)
	"""

	spinner = yaspin.yaspin(color="red")
	robot = RobotWrapper(spinner).init()

	curr_pos = robot.current()

	future_pos = curr_pos.copy()
	future_pos[posição] = valor + curr_pos[posição]

	printc(f"[&6ROBOT&f] &bEu estou em &dX: {curr_pos['x']}&b, &dY: {curr_pos['y']}&b, &dZ: {curr_pos['z']}")

	printc(f"[&6ROBOT&f] &bIndo para &dX: {future_pos['x']}&b, &dY: {future_pos['y']}&b, &dZ: {future_pos['z']}")

	#? Eu e meus casas garantindo segurança de tipos em Python
	robot.move(float(future_pos["x"]), float(future_pos["y"]), float(future_pos["z"]))

	printc(f"[&6ROBOT&f] &bCheguei!")

	robot.robot.close()

	return future_pos