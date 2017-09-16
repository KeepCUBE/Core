#!/usr/bin/python3

import sys
from config import INTERFACES
from _logging import Log

from communication import tcp, interfaces


class Core:
	def __init__(self):
		self.log = Log
		self.tcp_conn = tcp.create_server()
		self.interfaces = interfaces.Interfaces(INTERFACES)
