#! usr/bin/python


from Crypto.Cipher import AES
import base64 
from Crypto.Util.Padding import pad , unpad
from Crypto import Random


with open('encrypt_text.txt', 'w') as w:
	w.write('This is a dummy text for encryption using AES')
w.close()

with open('encrypt_text.txt', 'r') as r:
	plain_text=r.read()


key = b'ldhdnabvlowlmbhg'
block_size =  128
Init_vector = Random.new().read(16)
cipher = AES.new(key, AES.MODE_CBC, Init_vector)
Plain_text = bytes (plain_text,'UTF-8')
Cipher_text_bytes = cipher.encrypt(pad(Plain_text,AES.block_size))
Cipher_text = base64.b64encode(Cipher_text_bytes).decode()


print (f"{Init_vector = }\n{plain_text = }\n{Cipher_text = }")
r.close()




































