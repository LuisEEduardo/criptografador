from cryptography.fernet import Fernet
# EXEMPLO DE ENCRIPTAÇÃO E DESCRIPTAÇÃO
"""
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
plain_text = cipher_suite.decrypt(cipher_text)
"""

# Gerando chave 
chave = Fernet.generate_key()

cifra = Fernet(chave)

criptografando = cifra.encrypt(b"Mensagem secreta")
print(criptografando)

descriptografador = cifra.decrypt(criptografando)
print(descriptografador)

cript = Fernet(chave).encrypt(b'Mensagem secreta')
print(cript)
decript = Fernet(chave).decrypt(cript)
print(decript)

# Gerando a chave
# A chave é uma classe do tipo byte
chave = Fernet.generate_key()

print(chave)
print(type(chave))

# Converte a chave para um objeto cryptography.fernet.Fernet
cifrador = Fernet(chave)
print(cifrador)
print(type(cifrador))
