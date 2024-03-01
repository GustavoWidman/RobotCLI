import sys
import glob
import serial
from serial.tools import list_ports

def serial_ports():
    """
        Lista os dispositivos seriais disponíveis no sistema

        :raises EnvironmentError:
            Em caso de erro na detecção do sistema operacional
        :returns:
            Uma lista de portas seriais disponíveis
    """

    #? Windows
    if sys.platform.startswith('win'): ports = [port.device for port in list_ports.comports()]

    #? Linux
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # Exclude terminal device (/dev/tty)
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'): ports = glob.glob('/dev/tty.*')
    else: raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass

    return result