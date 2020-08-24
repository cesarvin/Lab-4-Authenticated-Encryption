# Abril Palencia - 18198
# Implementacion GCM

from Crypto.Cipher import AES

# Cifrado
# la key debe ser de 16 bytes
key = b'Mi llave cute :3'
data = b'Abril es la mejor del mundo mundial ntt'
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

print("Parte Cifrada")
print("Llave: " + str(key))
print("Nonce: " + str(nonce))
print("Ciphertext: " + str(ciphertext))
print("Mac - tag: " + str(tag))


# Descifrado
# prueba llave buena
key = b'Mi llave cute :3'
# prueba llave mala descomentar para probar
# key = b'Mi llave cuti :3'
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)

try:
    cipher.verify(tag)
    print("\nParte descifrada")
    print("Llave: " + str(key))
    print("Mac - tag: " + str(tag))
    print("El mensaje es autentico")
    print("El mensaje es: ", plaintext)
except ValueError:
    print("\nParte descifrada")
    print("La llave es incorrecta o el mensaje ha sido comprometido")