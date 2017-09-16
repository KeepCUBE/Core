from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver

from signal import signal, SIGINT, SIGTERM
from threading import Thread
from time import sleep, time
import random
from datetime import datetime

from jsonrpc import JSONRPCResponseManager, dispatcher
import json

import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")


@dispatcher.add_method
def test(echo):
	return 'jsonrpc: %s' % echo


@dispatcher.add_class
class Test:
	def test(self, echo):
		return 'class jsonrpc: %s' % echo


class System(Thread):
	kill = False

	def __init__(self):
		Thread.__init__(self)
		signal(SIGTERM, self.exit)
		signal(SIGINT, self.exit)
		self.start()

	start_time = datetime.now()

	# returns the elapsed milliseconds since the start of the program
	def millis(self):
		dt = datetime.now() - self.start_time
		ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
		return ms

	def exit(self, signum, frame):
		self.kill = True

	def run(self):
		while 1 and not self.kill:
			message = input('Message?')
			if random.choice([True, True]):
				reactor.callFromThread(Server.broadcast, message)
			else:
				reactor.callFromThread(Server.broadcast, "E_ON")
			# sleep(1)

		reactor.stop()


class Server(LineReceiver):
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
		response = JSONRPCResponseManager.handle(data, dispatcher)
		print(response.json)
		# print(data.decode('utf-8'))

	def send(self, data):
		if data is not None and isinstance(data, str):
			data = bytes(data, 'utf-8')

		self.sendLine(data)

	@classmethod
	def broadcast(cls, message):
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


System()
main()
