import sys
from cryptography.fernet import Fernet

#opening the key
with open('.code.key','rb') as filekey:
	key = filekey.read()
#using the generated key
fernet = Fernet(key)
#opening the file to ecnrypt
with open(sys.argv[1],'rb') as file:
	plaine = file.read()
#encrypting the file
encrypted = fernet.encrypt(plaine)
#saving the encrypted file
with open(sys.argv[2],'wb') as encrypted_file:
	encrypted_file.write(encrypted)
