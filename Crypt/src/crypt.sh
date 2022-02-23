#!/bin/bash

cd ../service/toCrypt/

if [[ ! -f "../service/toCrypt/*.txt" ]];
then
	cd ../../src/
	python3 encrypt.py ../service/toCrypt/*.txt ../service/Crypted/data-crypt.txt
	cp ../service/Crypted/data-crypt.txt ../service/toDecrypt/data-to-decrypt.txt
	cd ../service/toCrypt/
	rm *.txt
else
	echo "empty"
fi
