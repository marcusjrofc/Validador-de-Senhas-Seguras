import re

#Entrada
sua_senha = input("Digite sua senha:")

# 1. Mínimo de 8 caracteres
if len(sua_senha) < 8:
    print("Senha inválida: deve ter no mínimo 8 caracteres.")
    
# 2. Pelo menos uma letra maiúscula e uma minúscula
elif not re.search(r"[A-Z]",sua_senha) or not re.search(r"[a-z]",sua_senha):
    print("Erro: A senha deve conter pelo menos uma letra maiúscula e uma minúscula.")

# 3. Pelo menos um número
elif not re.search(r"\d",sua_senha):
    print("Erro: A senha deve conter pelo menos um número.")

# 4. Pelo menos um caractere especial (ex: !, @, #, $, %)
elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]",sua_senha):
    print("Erro: A senha deve conter pelo menos um caractere especial.")

# 5. Não pode conter "senha" ou "123456" (ignorando maiúsculas/minúsculas)
elif "senha" in sua_senha.lower() or "123456" in sua_senha.lower():
    print("Erro: A senha não pode conter as palavras 'senha' ou '123456'.")
else:
    print("Sucesso! Sua senha é forte e válida.")