from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineOnlyReceiver


class Client(LineOnlyReceiver):
	"""Once connected, send a message, then print the result."""

	def connectionMade(self):
		self.transport.write(b"hello, world!")

	# def dataReceived(self, line):
	# 	print(line)

	def lineReceived(self, line):
		print(line)

	def connectionLost(self, reason):
		print("connection lost")


class ClientFactory(protocol.ClientFactory):
	protocol = Client

	def clientConnectionFailed(self, connector, reason):
		print("Connection failed - goodbye!")
		reactor.stop()

	def clientConnectionLost(self, connector, reason):
		print("Connection lost - goodbye!")
		reactor.stop()


# this connects the protocol to a server running on port 8000

f = ClientFactory()
reactor.connectTCP("localhost", 8000, f)
reactor.run()
