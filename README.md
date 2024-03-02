# RobotCLI - Ponderada Gustavo Wagon Widman


## Descrição

Este projeto consiste no desenvolvimento de uma CLI (Command Line Interface) para controle de um robô DOBOT Magician Lite. A CLI também possui um comando "interface" que abre uma interface gráfica para controle do robô, transformando a CLI em uma interface híbrida.

---

## Instalação e execução

Para instalar as dependências do projeto, comece clonando o repositório

```bash
git clone https://github.com/GustavoWidman/RobotCLI.git
```

Depois, entre na pasta do projeto, crie um ambiente virtual (venv) e ative-o.

```bash
cd RobotCLI && python -m venv env && source env/bin/activate
```

Finalmente, instale as dependências do projeto com o comando:

```bash
pip install -r requirements.txt
```

Para rodar o projeto e visualizar os comandos disponíveis, execute:

```bash
$ python main.py --help


 Usage: main.py [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                  │
│ --show-completion             Show completion for the current shell, to copy it or       │
│                               customize the installation.                                │
│ --help                        Show this message and exit.                                │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────╮
│ atual              Mostra a posição atual do robô.                                       │
│ desligar           Desliga uma ferramenta específica.                                    │
│ home               Move o robô para a sua posição "home".                                │
│ interface          Chama a interface gráfica do robô.                                    │
│ ligar              Liga uma ferramenta específica.                                       │
│ mover              Move o robô para uma posição específica.                              │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
```

---

## Comandos

### `atual`

Esse comando mostra a posição atual do robô.

```bash
python main.py atual
```

### `mover`

Esse comando movimenta o robô em um eixo específico.

```bash
$ python main.py mover EIXO{x|y|z}

Valor: VALOR
```

Para mais informações, execute:

```bash
$ python main.py mover --help


 Usage: main.py mover [OPTIONS] EIXO:{x|y|z}

 Move o robô para uma posição específica
 - posicao: A posição que o robô deve se mover (x, y ou z)
 - valor: O valor que a posição deve ter
 Exemplo:
 $ python main.py mover x
 $ Valor: 100
 Isso adiciona 100 à posição X do robô (mantendo as posições Y e Z)

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────╮
│ *    eixo      EIXO:{x|y|z}  [default: None] [required]                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────╮
│ *  --valor        FLOAT  [default: None] [required]                                      │
│    --help                Show this message and exit.                                     │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
```

### `home`

Esse comando movimenta o robô para a posição de origem.

```bash
python main.py home
```

A posição de origem pode ser redefinida no arquivo `constants.json`.

### `ligar | desligar`

Esses comandos ligam e desligam uma ferramenta específica do robô.

```bash
python main.py ligar FERRAMENTA{suction|gripper}
```

```bash
python main.py desligar FERRAMENTA{suction|gripper}
```

### `interface`

Esse comando abre uma interface gráfica para controle do robô.

```bash
python main.py interface
```

Dentro dessa interface, é possível controlar o robô de forma gráfica com todas as funcionalidades disponíveis na CLI. Note que a presença do console continua sendo necessária, ja que ele é utilizado para mostrar informações mais detalhadas sobre o estado do robô.

## Estrutura do projeto

A estrutura do projeto é composta por pastas e arquivos que organizam os comandos, classes e utilitários. Segue abaixo a estrutura do projeto, resultado do comando `tree --gitignore`

```bash
.
├── classes
│   └── robot.py
├── commands
│   ├── atual.py
│   ├── ferramenta.py
│   ├── home.py
│   ├── interface.py
│   ├── mover.py
├── constants.json
├── interface
│   ├── main.py
├── main.py
├── README.md
├── requirements.txt
└── utils
    ├── ports.py
    └── text.py
```

## Demonstração

Segue abaixo um vídeo demonstrativo do funcionamento da CLI e da interface gráfica.

<video controls preload="none" width="100%" poster="https://files.r3dlust.com/s/pCeRBkHsoKwkKgS/preview">
 <source src="https://files.r3dlust.com/s/pCeRBkHsoKwkKgS/download" type="video/mp4">
</video>

[Link para o vídeo](https://links.r3dlust.com/robotcli-ponderada)
