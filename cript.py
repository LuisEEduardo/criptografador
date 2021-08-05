from cryptography.fernet import Fernet 


def gerar_chave(): 
    chave = Fernet.generate_key()
    return chave


def encriptando(): 
    t = texto()
    key = gerar_chave()
    cipher_suite = Fernet(key)
    texto_encrypt = cipher_suite.encrypt(t.encode())
    return key, texto_encrypt


def texto(): 
    print("""
    Opções: 
    1 - Para inserir o texto
    2 - Para colocar o caminho do arquivo .txt
    """)
    op = int(input('Insira a opção: '))
    if op == 1: 
        texto = input('Insira o texto: ')
        return texto
    elif op == 2: 
        nome_arquivo = input("Insira o caminho do arquivo: ")
        file = open(nome_arquivo, 'r')
        arquivo_ref = file.read()
        file.close()
        return arquivo_ref
    else: 
        print("Error")

c, t = encriptando()

print(f"A sua chave é: {c}\nO seu texto encriptado: {t}")
