from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineOnlyReceiver

import json

class Client(LineOnlyReceiver):
	"""Once connected, send a message, then print the result."""

	def connectionMade(self):
		payload = {
			"method": "test.test",
			"params": ["echome!"],
			"jsonrpc": "2.0",
			"id": 0,
		}
		self.transport.write(bytes(json.dumps(payload), 'utf-8'))

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
