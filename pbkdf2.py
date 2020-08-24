#Jorge Azmitia 15202
#PBKDF2

import os, binascii
from backports.pbkdf2 import pbkdf2_hmac


ans=True
while ans:
    print ("""
    1.Generate a key
    2.Exit/Quit
    """)
    ans=input("Seleccione una opcion: ")

    if ans=="1":
        password = input("Ingrese un password: ")
        salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
        passwd = password.encode("utf8")
        iteraciones = input("Ingrese numero de iteraciones que desea hacer")
        key = pbkdf2_hmac("sha256", passwd, salt, int(iteraciones), 32)
        print("Derived key:", binascii.hexlify(key))
    elif ans=="2":
        print("\n Gracias por utilizar el programa")
        exit()
