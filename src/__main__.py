#!/usr/bin/python3

from core import Core
from _logging import Log

Log.debug('Main')

Log.debug('Starting core')
core = Core()



# from signal import signal, SIGINT, SIGTERM
# from threading import Thread
# from time import sleep, time
# import random
# from datetime import datetime


# class System(Thread):
# 	kill = False
#
# 	def __init__(self):
# 		Thread.__init__(self)
# 		signal(SIGTERM, self.exit)
# 		signal(SIGINT, self.exit)
# 		self.start()
#
# 	start_time = datetime.now()
#
# 	# returns the elapsed milliseconds since the start of the program
# 	def millis(self):
# 		dt = datetime.now() - self.start_time
# 		ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
# 		return ms
#
# 	def exit(self, signum, frame):
# 		self.kill = True
#
# 	def run(self):
# 		while 1 and not self.kill:
# 			message = input('Message?')
#
# 			# sleep(1)
#
# 		reactor.stop()
