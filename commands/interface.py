from utils.text import printc
import flet as ft
from interface.main import main
import typer
import sys


app = typer.Typer()


@app.command(short_help="Chama a interface gráfica do robô.")
def interface(view = None):
	"""
		Chama a interface gráfica do robô

		Exemplo:

			$ python main.py interface

			Isso abrirá a interface gráfica do robô
	"""
	if view is not None and view is not "web":
		raise ValueError("Apenas \"web\" é suportado como visualização.")

	if view is "web": ft.app(target=main, view=ft.AppView.WEB_BROWSER)

	#? Camada de compatibilidade com sistemas operacionais
	if sys.platform.startswith('win'):
		ft.app(target=main)
	elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
		ft.app(target=main, view=ft.AppView.WEB_BROWSER)
	elif sys.platform.startswith('darwin'):
		printc("[&6ROBOT&f] &cEssa interface gráfica não foi testada no seu sistema operacional, caso encontre problemas, adicione \"--view=web\" ao comando.")
		ft.app(target=main)