import serial
from threading import Thread

#from config import INTERFACES as config



class Interfaces:
	"""docstring for Interface"""

	def __init__(self):
		print('IF: construct')
#		self._baud = config['SERIAL']['baud']
#		self._ser_port = config['SERIAL']['port']
		self._baud = 9600
		self._ser_port = "/dev/ttyS0"


	def set_serial(self, port, baud):
		print("IF: serial set")
		self._ser_port = port
		self._baud = baud

	def init(self):
		print('IF: init')
		self._ser_conn = Serial(self._ser_port,self._baud)
		self.nrf = NRF(self._ser_conn)

class NRF:
	def __init__(self, serial):
		self.serial = serial

	def send(self, data):
		print(data)


class Serial:
	ser = None
	def __init__(self, com='/dev/ttyS4', baud=9600):
		print('serial: construct')
		global ser
		ser = serial.Serial(port=com, baudrate=baud, timeout=2)
		if ser.isOpen(): ser.close()
		ser.open()
		#Thread(target = self.listen).start()

	def listen(self):
		print("serial: listen")
		while True:
			byte = ser.read(1)
			if byte:
				print(byte.decode())

	@staticmethod
	def send(data):
		print(ser.write(data.encode()))

	def __del__(self):
		print('serial: destruct')
		ser.close()

ifaces = Interfaces()
ifaces.init()
ifaces.nrfs.send("ahoj")