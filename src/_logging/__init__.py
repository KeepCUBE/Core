import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


class Log:
	@staticmethod
	def debug(message):
		logging.debug(message)
