# Cryptage

## The objective of the program

## - To crypt and decrypt files manually 
>The user can select their files from a location and store the encrypted data in another directory.
> To decrypt it also, they will have to use the terminal to decrypt the data.
## To crypt and decrypt files using installation files
> The user can execute the script which will encrypt the files and decrypt it also.

# Languages used:
| Files | Langueage |
| ------ | ------ |
| Crypt.sh | Bash Script|
| Crypt.py | Python |
| Crypt.service | Command line |
| Decrypt.sh |Bash Script|
| Decrypt.service | Command line |
| Decrypt.py | Python |
| key.py | Python |

## To encrypt and decrypt files manually:
##### Suppose there are 2 folders, Folder A containing the raw file and Folder B is the folder to keep the encrypted data and decrypted data
- Go to crypt/src/
- Open terminal in the directory
- type "python3 encrypt.py /FolderA/original.txt /FolderB/crypted.txt"
- The first arguement is the location of the original data while the second arguement is where to save and the name of the crypted data
- To decrypt the data, still in the src directory
- "python3 decrypt.py /FolderB/crypted.txt /FolderB/decrypted.txt"

## To encrypt and decrypt using the installation file
##### Suppose there are 2 folders, Folder A containing the raw file and Folder B is the folder to keep the encrypted data and decrypted data
- First the user will have to locate the installation file and launch the terminal
- In the terminal, type "./install"
- It is a bash script but it does not require the extension because the shabang is more important
- The raw data will encrypt the data and decrypt it in one single click
- The original data will be deleted but the encrypted data will be saved as well as a new decrypted data.
## To uninstall the file from the pc
First the user will have to locate the uninstall file
- In the terminal, type "./uninstall"


