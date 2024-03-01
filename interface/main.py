import flet as ft
from commands.mover import mover
from commands.atual import atual
from commands.home import home
from commands.ferramenta import ligar, desligar

def main(page: ft.Page):
	page.title = "RobotCLI Ponderada"
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.theme_mode = ft.ThemeMode.DARK

	pos_value = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=200, label="Valor")
	pos_type = ft.Dropdown(
		width=150,
		label="Eixo",
		options=[
			ft.dropdown.Option("X"),
			ft.dropdown.Option("Y"),
			ft.dropdown.Option("Z"),
		],
		value="X",
	)
	move_output = ft.Text("", size=20, text_align=ft.TextAlign.CENTER)
	home_output = ft.Text("", size=20, text_align=ft.TextAlign.CENTER)
	atual_output = ft.Text("", size=20, text_align=ft.TextAlign.CENTER)
	ferramentas_type = ft.Dropdown(
		width=150,
		label="Ferramenta",
		options=[
			ft.dropdown.Option("Suction"),
			ft.dropdown.Option("Gripper"),
		],
		value="Suction",
	)
	ferramentas_value = ft.Switch(value=False, width=100)
	ferramentas_output = ft.Text("", size=20, text_align=ft.TextAlign.CENTER)

	def mover_app(e):
		pos_value.value = str(int(pos_value.value))
		move_output.value = "Movendo..."
		page.update()
		try:
			new_pos = mover(pos_type.value.lower(), float(pos_value.value))
			move_output.value = f"Operação realizada com sucesso: \nRobô movido para a posição X: {new_pos['x']}, Y: {new_pos['y']}, Z: {new_pos['z']}."
			page.update()
		except Exception as e:
			print(e)
			move_output.value = "Erro ao mover o robô! Verifique o console para mais informações."
			page.update()

	def home_app(e):
		home_output.value = "Movendo..."
		page.update()
		try:
			home()
			home_output.value = "Operação realizada com sucesso! \nRobô movido para a posição HOME."
			page.update()
		except Exception as e:
			print(e)
			home_output.value = "Erro ao mover o robô! Verifique o console para mais informações."
			page.update()

	def atual_app(e):
		atual_output.value = "Atualizando..."
		page.update()
		try:
			output = atual()
			atual_output.value = f"Posição atual: X: {output['x']}, Y: {output['y']}, Z: {output['z']}"
			page.update()
		except Exception as e:
			print(e)
			atual_output.value = "Erro ao atualizar o robô! Verifique o console para mais informações."
			page.update()

	def ferramentas_app(e):
		try:
			if ferramentas_value.value:
				ligar(ferramentas_type.value.lower())
			else:
				desligar(ferramentas_type.value.lower())
			ferramentas_output.value = f"Operação realizada com sucesso! \nFerramenta {ferramentas_type.value.upper()} {'ligada' if ferramentas_value.value else 'desligada'}."
			page.update()
		except Exception as e:
			print(e)
			ferramentas_output.value = "Erro ao ligar ou desligar a ferramenta! Verifique o console para mais informações."
			page.update()


	page.add(
		ft.Row([ft.Text("Mover ", size=25)], alignment=ft.MainAxisAlignment.CENTER),
		ft.Row(
			[
				pos_type,
				pos_value,
				ft.IconButton(ft.icons.RUN_CIRCLE, on_click=mover_app, icon_size=40),
			],
			alignment=ft.MainAxisAlignment.CENTER,
		),
		ft.Row([move_output], alignment=ft.MainAxisAlignment.CENTER),
		ft.Row([ft.Text("Ferramentas", size=25)], alignment=ft.MainAxisAlignment.CENTER),
		ft.Row(
			[
				ferramentas_type,
				ferramentas_value,
				ft.IconButton(ft.icons.PAN_TOOL_ALT, on_click=ferramentas_app, icon_size=40),
			],
			alignment=ft.MainAxisAlignment.CENTER,
		),
		ft.Row([ferramentas_output], alignment=ft.MainAxisAlignment.CENTER),
		ft.Row([ft.Text("Home", size=25)], alignment=ft.MainAxisAlignment.CENTER),
		ft.Row(
			[
				ft.IconButton(ft.icons.HOME, on_click=home_app, icon_size=40),
			],
			alignment=ft.MainAxisAlignment.CENTER,
		),
		ft.Row([home_output], alignment=ft.MainAxisAlignment.CENTER),
		ft.Row([ft.Text("Atual", size=25)], alignment=ft.MainAxisAlignment.CENTER),
		ft.Row(
			[
				ft.IconButton(ft.icons.REFRESH, on_click=atual_app, icon_size=40),
			],
			alignment=ft.MainAxisAlignment.CENTER,
		),
		ft.Row([atual_output], alignment=ft.MainAxisAlignment.CENTER),
	)