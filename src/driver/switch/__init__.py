from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineOnlyReceiver


class Client(LineOnlyReceiver):
	"""Once connected, send a message, then print the result."""

	def connectionMade(self):
		self.transport.write(b'Switch driver registered')

	def lineReceived(self, line):
		if line.startswith(b'E_'):
			self.transport.write(b'Event handled')
		else:
			print(line.decode('utf-8'))

	def connectionLost(self, reason):
		print("connection lost")


f = protocol.ClientFactory.forProtocol(Client)
reactor.connectTCP("localhost", 8000, f)
reactor.run()
