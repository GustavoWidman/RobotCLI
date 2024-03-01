from classes.robot import RobotWrapper
from utils.text import printc, cstring
import typer
import yaspin


app = typer.Typer()

@app.command(short_help="Mostra a posição atual do robô.")
def atual():
	"""
		Mostra a posição atual do robô

		Exemplo:

			$ python main.py atual

			Isso mostrará a posição atual do robô (X, Y, Z)
	"""

	spinner = yaspin.yaspin(color="red")
	robot = RobotWrapper(spinner).init()

	curr_pos = robot.current()

	printc(f"[&6ROBOT&f] &bEu estou em &dX: {curr_pos['x']}&b, &dY: {curr_pos['y']}&b, &dZ: {curr_pos['z']}")

	robot.robot.close()

	return curr_pos