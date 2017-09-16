import json


class Notification:
	@staticmethod
	def send(id, notify_type, title, content, color="#ff0000"):
		if (id >= 2147483647) and (id < 0):
			raise ValueError("Notification ID exceeds 4 bytes")
		else:
			print(json.dumps(
				[{
					'type': 'notification',
					'data': {'id': id, 'type': notify_type, 'title': title, 'content': content, 'color': color}
				}]))
