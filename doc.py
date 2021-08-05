from cryptography.fernet import Fernet

# Gerando a chave
chave = Fernet.generate_key()

# Converte a chave para um objeto cryptography.fernet.Fernet
cifrador = Fernet(chave)

# Abrindo o arquivo texto 
nome_arquivo = "./texto.txt"
ref_arquivo = open(nome_arquivo, "r")
texto = ref_arquivo.read()
ref_arquivo.close() 

# Criptografando o arquivo 
texto_cript = cifrador.encrypt(texto.encode())
# print(texto_cript)

# Reescrevendo o arquivo agora criptografado
nome_arquivo = "./texto.txt"
ref_arquivo = open(nome_arquivo, 'wb')
escrevendo = ref_arquivo.write(texto_cript)
ref_arquivo.close()

# Descriptografando o arquivo 
texto_decript = cifrador.decrypt(texto_cript)
# print(texto_decript)

# Abrindo o arquivo e descriptografando ele  
nome_arquivo = "./texto.txt"
ref_arquivo = open(nome_arquivo, 'rb')
texto = ref_arquivo.read()
ref_arquivo.close()

texto_decript = cifrador.decrypt(texto)
print(texto)
