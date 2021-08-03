from cryptography.fernet import Fernet

# Gerando a chave
chave = Fernet.generate_key()

# Converte a chave para um objeto cryptography.fernet.Fernet
cifrador = Fernet(chave)



