import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


class Log:
	def debug(self, message):
		logging.debug(message)
