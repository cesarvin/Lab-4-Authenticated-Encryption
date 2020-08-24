# implementación de argon2
import argon2



while True:
    print("""1. Generar una llave
2. Salir del programa""")
    ele = int(input("Ingrese su elección: "))

    
    if ele == 1:
        psw = input("Ingrese la contraseña maestra: ")
        passhasher = argon2.PasswordHasher()
        hashed = passhasher.hash(psw)
        print("La nueva contraseña es:",hashed)
        print("\n Ahora verificando...")
        verificacion=passhasher.verify(hashed,psw)

        
        if verificacion:
            print("La verificación ha sido exitosa :)")
        else:
            print("La verificación ha fallado :(")
        print("\n"*4)

    else:
        print("Saliendo del programa...")
        break
