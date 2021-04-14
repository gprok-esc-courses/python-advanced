import json

message = {
    'type': 'joined',
    'name': 'Mark'
}

message_json = json.dumps(message)

print(message_json)

msg = json.loads(message_json)

print(msg['type'])
