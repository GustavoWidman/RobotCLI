from typing_extensions import Annotated
import flet as ft
from interface.main import main
import typer


app = typer.Typer()


@app.command(short_help="Chama a interface gráfica do robô.")
def interface():
	"""
		Chama a interface gráfica do robô

		Exemplo:

			$ python main.py interface

			Isso abrirá a interface gráfica do robô
	"""

	ft.app(target=main, view=ft.AppView.WEB_BROWSER)