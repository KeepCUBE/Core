import json

msgType = "notification"
ntfType = "warn"
title = "nadpis"
content = "obsah"
color = None


print(json.dumps([{'type': msgType, 'data': {'type': ntfType, 'title': title, 'content': content, 'color': color}}]))
