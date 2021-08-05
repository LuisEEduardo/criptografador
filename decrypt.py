from cryptography.fernet import Fernet

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def descriptografando(): 
    chave = input("Insira a chave: ")
    texto = input('Insira o texto: ')
    texto_decrypt = Fernet(chave.encode()).decrypt(texto.encode())
    clear()
    print('-=' * 30)
    print(f"Texto descriptografado: \n{texto_decrypt}")
    print('-=' * 30)

descriptografando()
