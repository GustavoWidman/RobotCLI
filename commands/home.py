from classes.robot import RobotWrapper
from utils.text import printc, cstring
import typer
import yaspin


app = typer.Typer()

@app.command(short_help="Move o robô para a sua posição \"home\".")
def home():
	"""
		Move o robô para a sua posição "home"

		Exemplo:

			$ python main.py home

			Isso moverá o robô para a posição X: 100, mantendo as posições Y e Z
	"""

	spinner = yaspin.yaspin(color="red")
	robot = RobotWrapper(spinner).init()

	curr_pos = robot.current()

	printc(f"[&6ROBOT&f] &bEu estou em &dX: {curr_pos['x']}&b, &dY: {curr_pos['y']}&b, &dZ: {curr_pos['z']}")

	printc(f"[&6ROBOT&f] &bIndo para &dHOME &b(&dX: {robot.constants['home']['x']}&b, &dY: {robot.constants['home']['y']}&b, &dZ: {robot.constants['home']['z']}&b)")

	robot.home()

	printc(f"[&6ROBOT&f] &bCheguei!")

	robot.robot.close()