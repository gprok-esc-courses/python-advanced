import rsa

public_key, private_key = rsa.newkeys(512)

print(public_key)
print(private_key)

message = 'Hello World!'
message_bytes = message.encode('utf8')
message_enc = rsa.encrypt(message_bytes, public_key)

print(message_enc)

msg_bytes = rsa.decrypt(message_enc, private_key)
msg = msg_bytes.decode('utf8')

print(msg)


