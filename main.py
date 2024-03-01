import typer

from commands.mover import app as mover
from commands.home import app as home
from commands.atual import app as atual
from commands.ferramenta import app as ferramenta
from commands.interface import app as interface

app = typer.Typer()

app.registered_commands += mover.registered_commands
app.registered_commands += home.registered_commands
app.registered_commands += atual.registered_commands
app.registered_commands += ferramenta.registered_commands
app.registered_commands += interface.registered_commands


if __name__ == "__main__":
	#? Isso daqui é só pra dar um espaço entre o comando e as mensagens do terminal (pra ficar mais bonito)
	print("")
	app()