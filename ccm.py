from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# variables para completar el cifrado
hdr = b'hdr oculto para cifrado'
key = b'Llave para cifrar en bytes'
nonce = get_random_bytes(11)

ans=True
while ans:
    print ("""
    1. Generar mensaje
    2. Decifrar mensaje
    3.Exit/Quit
    """)
    ans=input("Seleccione una opcion: ")

    if ans=="1":
        # se solicita el texto para enviar
        text = input('\nIngrese un texto: ')
        
        # se convierte en string bytes
        plaintext = bytes(text, encoding='utf-8')
        
        #se genera el mensaje utilizando CCM mode
        cipher = AES.new(key, AES.MODE_CCM, nonce)
        cipher.update(hdr)
        msg = nonce, hdr, cipher.encrypt(plaintext), cipher.digest()

        print ('\nEl mensaje que se ha enviado es:\n')
        print (msg)

    elif ans=="2":
        
        print ('\nSe decodifica el mensaje recibido:\n')
        print (msg)
        
        # se obtienen los datos del mensaje
        nonce, hdr, ciphertext, mac = msg
        
        # se decifra el mensaje para obtener el texto plano usando CCM mode 
        cipher = AES.new(key, AES.MODE_CCM, nonce)
        cipher.update(hdr)
        plaintext = cipher.decrypt(ciphertext)

        print('\nEl mensaje es:\n') 
        print(plaintext.decode('UTF-8','Ignore'))
        
    elif ans=="3":
        print("\n Gracias por utilizar el programa")
        exit()
