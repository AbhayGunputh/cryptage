#!/bin/bash

cd ../service/toDecrypt/

if [[ ! -f "../service/toDecrypt/data-to-decrypt.txt" ]];
then
        cd ../../src/
        python3 decrypt.py ../service/toDecrypt/data-to-decrypt.txt ../service/Decrypted/data.txt
	cd ../service/toDecrypt/
	rm data-to-decrypt.txt
else
        echo "empty"
fi

