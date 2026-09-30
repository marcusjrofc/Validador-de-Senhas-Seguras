#Validador de Senhas Seguras 🔐

Este é um projeto simples em Python desenvolvido para validar a força de senhas. O script recebe uma entrada do usuário e verifica se a senha atende a critérios específicos de segurança.

📋 Regras de Validação

Para que a senha seja considerada "forte e válida", ela deve obrigatoriamente cumprir todas as seguintes regras:

Ter no mínimo 8 caracteres.

Conter pelo menos uma letra maiúscula (A-Z) e uma letra minúscula (a-z).

Conter pelo menos um número (0-9).

Conter pelo menos um caractere especial (ex: !, @, #, $, %, etc.).

Não conter palavras óbvias, como "senha" ou "123456" (ignorando se as letras estão em maiúsculo ou minúsculo).

🚀 Como executar o projeto

Pré-requisitos

Você precisa ter o Python instalado no seu computador.

Passos

Clone este repositório ou baixe os arquivos.

Abra o terminal (ou prompt de comando) e navegue até a pasta do projeto.

Execute o seguinte comando:

python main.py


Digite uma senha quando o terminal pedir e veja o resultado da validação!

🛠️ Tecnologias Utilizadas

Python 3

Módulo re (Expressões Regulares nativas do Python) para a busca de padrões nos caracteres.