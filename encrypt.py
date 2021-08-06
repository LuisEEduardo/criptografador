from cryptography.fernet import Fernet 


def clean():
    import os 
    os.system('cls' if os.name == "nt" else "clear")


def gerar_chave(): 
    chave = Fernet.generate_key()
    return chave


def encriptando(): 
    t, opcao, n = texto()
    key = gerar_chave()
    cipher_suite = Fernet(key)
    texto_encrypt = cipher_suite.encrypt(t.encode())
    if opcao == 2: 
        escrevendo(texto=texto_encrypt, caminho=n)
    return key, texto_encrypt


def escrevendo(texto, caminho): 
    file = open(caminho, 'wb')
    file.write(texto)
    file.close()


def ler_arquivo(): 
    nome_arquivo = input("\nInsira o caminho do arquivo: ")
    file = open(nome_arquivo, 'r')
    arquivo_ref = file.read()
    file.close()
    return nome_arquivo, arquivo_ref


def texto(): 
    clean()
    print("Opções: \n1 - Para inserir o texto \n2 - Para colocar o caminho do arquivo .txt")
    op = int(input('Insira a opção: '))
    nome_arquivo = "sem"
    if op == 1: 
        texto = input('\nInsira o texto: ')
        return texto, op, nome_arquivo 
    elif op == 2: 
        nome_arquivo, texto = ler_arquivo()
        return texto, op, nome_arquivo
    else: 
        print("Error")


c, t = encriptando()

clean()
print(f"A sua chave é: {c}\nO seu texto encriptado: {t}")
