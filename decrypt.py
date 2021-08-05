from cryptography.fernet import Fernet

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def descriptografando(): 
    chave = input("Insira a chave: ")
    print("""
    Opção: 
    1 - Para inserir o texto no terminal
    2 - Para inserir o caminho do arquivo .txt
    """)

    op = int(input("Insira a opção: "))
    if op == 1:
        texto = input('Insira o texto criptografado: ')
        texto_decrypt = Fernet(chave.encode()).decrypt(texto.encode())
    elif op == 2:
        print()
        nome_arquivo = input("Insira o caminho do arquivo: ")
        file = open(nome_arquivo, 'rb')
        texto = file.read()
        file.close()
        texto_decrypt = Fernet(chave.encode()).decrypt(texto)
    else: 
        texto_decrypt = "Error"
    clear()
    print('-=' * 30)
    print(f"Texto descriptografado: \n{texto_decrypt}")
    print('-=' * 30)



descriptografando()
