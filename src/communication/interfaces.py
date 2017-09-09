import serial
from threading import Thread

class ifaces:
	"""docstring for Interface"""
	_ser_port='/dev/ttyS0'

	def __init__(self):
		print('IF: construct')

	def setSerial(self,port = '/dev/ttyS0',baud = 9600):
		print ("IF: serial set")
		self._ser_port = port
		self._baud = baud
		
	def init(self):
		print('IF: init')
		self._ser_conn = self.serial(self._ser_port,self._baud)

	class serial:
		ser = None
		def __init__(self,com,baud):
			print('serial: construct')
			global ser 
			ser = serial.Serial(port=com,baudrate=baud, timeout=2)
			if ser.isOpen(): ser.close()
			ser.open()
			#Thread(target = self.listen).start()
			
		def listen(self):
			print("serial: listen")
			while True:
				byte = ser.read(1)
				if byte: print(byte.decode())

		@staticmethod
		def send(data):
			print(ser.write(data.encode()))

		def __del__(self):
			print('serial: destruct')
			ser.close()
			

output = ifaces()
output.setSerial('/dev/ttyS0',9600)
output.init()
#output.serial.send("...")