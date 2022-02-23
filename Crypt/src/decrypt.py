import sys
from cryptography.fernet import Fernet

#opening the key
with open('.code.key','rb') as filekey:
	key = filekey.read()
#using the generated key
fernet = Fernet(key)
#opening the file to decrypt
with open(sys.argv[1],'rb') as enc_file:
	cipher = enc_file.read()
#decrypting the file
decrypted = fernet.decrypt(cipher)
#saving the decrypted file
with open(sys.argv[2],'wb') as dec_file:
	dec_file.write(decrypted)
