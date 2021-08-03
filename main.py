from cryptography.fernet import Fernet


# Criando uma chave 
chave = Fernet.generate_key()  # Gerando uma chave randômica

print(f'A chave criada foi {chave}')

# Armazenando Chave no arquivo .key
file = open('chave.key', 'wb')
file.write(chave)
file.close()

# Acessando e Lendo o arquivo da chave .key
file = open('chave.key', 'rb')
lendo_chave = file.read()
file.close()

print(f'\nA chave lida foi {lendo_chave}')

# EXEMPLO DE ENCRIPTAÇÃO E DESCRIPTAÇÃO
"""
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
plain_text = cipher_suite.decrypt(cipher_text)
"""
