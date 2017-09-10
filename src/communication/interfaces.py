# import serial
from threading import Thread



from config import INTERFACES as config

class Interfaces:
	"""docstring for Interface"""

	def __init__(self):
		print('IF: construct')
		self._baud = config['SERIAL']['baud']
		self._ser_port = config['SERIAL']['port']

	def set_serial(self, port='/dev/ttyS0', baud=9600):
		print("IF: serial set")
		self._ser_port = port
		self._baud = baud

	def init(self):
		print('IF: init')
		self._ser_conn = self.Serial(self._ser_port,self._baud)

	class Serial:
		ser = None

		def __init__(self, com='/dev/ttyS0', baud=9600):
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
