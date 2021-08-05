from cryptography.fernet import Fernet 


def gerar_chave(): 
    chave = Fernet.generate_key()
    return chave


def encriptando(texto): 
    key = gerar_chave()
    cipher_suite = Fernet(key)
    texto_encrypt = cipher_suite.encrypt(texto.encode())
    return key, texto_encrypt


texto = input("Insira o texto: ")
c, t = encriptando(texto)

print(f"A sua chave é: {c}\nO seu texto encriptado: {t}")
