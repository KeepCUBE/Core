from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver

import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")


class _Server(LineReceiver):
	"""This is just about the simplest possible protocol"""
	conn = None
	clients = []
	conn_n = 0

	def __init__(self, clients):
		Server.clients.append(self)

	# self.clients = clients

	def connectionMade(self):
		logging.debug('Client connected - %d' % Server.conn_n)
		Server.conn_n += 1
		# self.send('Hello')

	def lineReceived(self, line):
		pass

	def dataReceived(self, data):
		print(data.decode('utf-8'))

	def send(self, data):
		if data is not None and isinstance(data, str):
			data = bytes(data, 'utf-8')

		self.sendLine(data)

	@classmethod
	def broadcast(cls, message):
		for client in cls.clients:
			client.send(message)


class _ServerFactory(protocol.Factory):
	def __init__(self):
		self.clients = []

	def buildProtocol(self, addr):
		return _Server(self.clients)


class TCP:
	def __init__(self):
		reactor.listenTCP(8000, _ServerFactory())
		reactor.run()
		self.conn = reactor

	@staticmethod
	def broadcast(self, message):
		reactor.callFromThread(_Server.broadcast, message)


def create_server():
	"""This runs the protocol on port 8000"""
	return TCP()
