from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver

# from threading import Thread
# from time import sleep

import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")


# class System(Thread):
# 	def __init__(self):
# 		Thread.__init__(self)
# 		self.start()
#
# 	def run(self):
# 		while 1:
# 			reactor.callFromThread(Server.broadcast, "hello world")
# 			sleep(1)

class Server(LineReceiver):
	"""This is just about the simplest possible protocol"""
	conn = None
	clients = []

	def __init__(self, clients):
		Server.clients.append(self)

	# self.clients = clients

	def connectionMade(self):
		logging.debug('Client connected')
		# self.conn = Connection(self.transport)
		self.send('Hello')

	def lineReceived(self, line):
		pass

	def rawDataReceived(self, data):
		pass

	def send(self, data):
		if data is not None and isinstance(data, str):
			data = bytes(data, 'utf-8')

		self.sendLine(data)

	@classmethod
	def broadcast(cls, message):
		print(cls.clients)
		for client in cls.clients:
			client.send(message)


class ServerFactory(protocol.Factory):
	def __init__(self):
		self.clients = []

	def buildProtocol(self, addr):
		return Server(self.clients)


def main():
	"""This runs the protocol on port 8000"""
	reactor.listenTCP(8000, ServerFactory())
	reactor.run()


main()
