from yaspin import yaspin
from utils.text import cstring, printc
from utils.ports import serial_ports
from lib.pydobot import Dobot
import json
import os



class RobotWrapper:
	def __init__(self, spinner: yaspin):
		printc("[&6ROBOT&f] &bInstanciando classe do robô...")
		with open("constants.json", "r") as f:
			self.constants = json.load(f)

		self.initialized = False
		self.spinner = spinner


	def init(self):
		"""
			Inicializa a conexão com o robô
		"""
		printc("[&6ROBOT&f] &bEstabelecendo conexão com o robô...")

		self.spinner.start()
		self.spinner.text = cstring("[&6ROBOT&f] &bBuscando a porta do robô...")

		self.port = self.scan_ports()

		self.robot = Dobot(port=self.port)
		printc(f"[&6ROBOT&f] &aConectado ao robô na porta &5{self.port}")

		self.initialized = True
		self.update_pos()

		return self


	def scan_ports(self) -> str:
		"""
			Procura por portas seriais disponíveis e tenta conectar com o robô
		"""
		ports = serial_ports()
		for port in ports:
			self.spinner.text = cstring(f"[&6ROBOT&f] &bProcurando robô na porta &5{port}")
			try:
				Dobot(port=port).close()

				self.spinner.stop()
				printc(f"[&6ROBOT&f] &aRobô encontrado na porta &5{port}")

				return port
			except Exception as e:
				if ("Permission denied" in str(e)):
					self.spinner.stop()
					printc(f"[&6ROBOT&f] &cErro de permissão, tente rodar o programa como administrador.")
					os._exit(1)
				else: continue

		self.spinner.stop()
		printc("[&6ROBOT&f] &cNenhum robô foi encontrado, por favor, verifique a conexão ou conecte um robô para prosseguir.")
		os._exit(1)


	def update_pos(self) -> None:
		if not self.initialized: self.init()
		self.x, self.y, self.z, self.r, self.j1, self.j2, self.j3, self.j4 = self.robot.pose()


	def move(self,
		x: float | None = None,
		y: float | None = None,
		z: float | None = None,
		r: float | None = None
	) -> None:
		if not self.initialized: self.init()

		if x is None: x = self.x
		if y is None: y = self.y
		if z is None: z = self.z
		if r is None: r = self.r

		self.spinner.start()
		self.spinner.text = cstring(f"[&6ROBOT&f] &bMovendo robô para (&5{x}&b, &5{y}&b, &5{z}&b)")

		self.robot.move_to(x, y, z, r, wait=True)

		self.spinner.stop()
		self.update_pos()


	def current(self) -> dict[str, float]:
		self.update_pos()
		return { "x": round(self.x, 2), "y": round(self.y, 2), "z": round(self.z, 2) }


	def tool(self, tool: str, state: bool) -> None:
		if not self.initialized: self.init()

		printc(f"[&6ROBOT&f] &bLigando a ferramenta &5{tool}")

		match tool:
			case "suction":
				self.robot.suck(state)
			case "gripper":
				self.robot.grip(state)
			case _:
				printc(f"[&6ROBOT&f] &cFerramenta &5{tool} &cnão encontrada.")
				return

		printc(f"[&6ROBOT&f] &bFerramenta &5{tool} &b{'ligada' if state else 'desligada'}")



	def home(self):
		if not self.initialized: self.init()
		self.move(self.constants['home']['x'], self.constants['home']['y'], self.constants['home']['z'])