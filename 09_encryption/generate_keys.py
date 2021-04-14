import rsa

public_key, private_key = rsa.newkeys(512)

public_file = open("public.txt", "w")
public_file.write(public_key.save_pkcs1().decode('utf8'))
public_file.close()

private_file = open("private.txt", "w")
private_file.write(private_key.save_pkcs1().decode('utf8'))
private_file.close()
