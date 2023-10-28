# VERIFICAÇÃO DE STRINGS COM PYTHON 
# A verificação de strings em Python pode ser feita de várias maneiras, dependendo do que você precisa verificar. Aqui estão algumas das operações mais comuns de verificação 
# de strings em Python: 

# Verificar se uma Substring está em uma String: Use o operador in para verificar se uma substring está presente em uma string.
texto = "Isso é uma string de exemplo"
if "exemplo" in texto:
    print("A substring 'exemplo' está na string.")

# Verificar o Comprimento de uma String: se a função len() para obter o comprimento de uma string.
texto = "Isso é uma string de exemplo"
comprimento = len(texto)
print(f"O comprimento da string é {comprimento}.")

# Verificar se uma String Começa ou Termina com uma Substring: Use os métodos .startswith() e .endswith() para verificar se uma string começa ou termina com uma determinada substring.
texto = "Isso é uma string de exemplo"
if texto.startswith("Isso"):
    print("A string começa com 'Isso'.")

if texto.endswith("exemplo"):
    print("A string termina com 'exemplo'.")

# Verificar se uma String é Numérica: Use o método .isnumeric() para verificar se uma string é composta apenas por caracteres numéricos.
numero = "12345"
if numero.isnumeric():
    print("A string contém apenas dígitos numéricos.")

# Verificar se uma String é Alfabética: Use o método .isalpha() para # Verificar se uma string contém apenas letras do alfabeto.
palavra = "Python"
if palavra.isalpha():
    print("A string contém apenas letras do alfabeto.")

# Verificar se uma String é Alfanumérica: Use o método .isalnum() para verificar se uma string é composta apenas por caracteres alfanuméricos (letras e números).
texto = "Python123"
if texto.isalnum():
    print("A string contém apenas caracteres alfanuméricos.")

# Os métodos startswith() e endswith() em Python são usados para verificar se uma string começa ou termina com um determinado prefixo ou sufixo, respectivamente. 
# Ambos os métodos retornam um valor booleano (True ou False) indicando se a string atende aos critérios especificados.A sintaxe básica dos métodos startswith() e endswith():
# string.startswith(prefixo)
# string.endswith(sufixo)

# Onde: string é a string que você deseja verificar.
# prefixo é a substring que você deseja verificar se a string começa com ela.
# sufixo é a substring que você deseja verificar se a string termina com ela. Aqui estão exemplos de uso desses métodos:

# Exemplo do método startswith():
frase = "Olá, mundo!"
if frase.startswith("Olá"):
    print("A frase começa com 'Olá'.")
else:
    print("A frase não começa com 'Olá'.")

# # Exemplo do método `endswith()`: 
frase = "Isso é um exemplo."
if frase.endswith("exemplo."):
    print("A frase termina com 'exemplo.'.")
else:
    print("A frase não termina com 'exemplo.'.")

# Neste exemplo, o método `endswith()` verifica se a string `frase` termina com a substring "exemplo.".
# Você também pode especificar um índice de início e fim para limitar a pesquisa a uma parte específica da string. Por exemplo:

frase = "Isso é um exemplo."
if frase.startswith("exemplo", 10):
    print("A substring 'exemplo' começa na posição 10 da frase.")

# Neste exemplo, o método `startswith()` verifica se a substring "exemplo" começa a partir da posição 10 da string `frase`.
# Esses métodos são úteis para realizar verificações condicionais com base no início ou no final de uma string em Python.

# MANIPULANDO STRINGS EM PYTHON

cidade = 'São Carlos'
endereco = 'Rua Cândido Padim, 25 - Vila Prado'
completo = cidade + endereco
print(cidade.startswith('São'))
print(cidade.endswith('los'))

print('Rua' in completo)
print('Padim' not in completo)

# Exemplo 01: Preciso de sistema que verifique se existe, no texto a palavra gmail se existir, printe-as:

email = "senai@gmail.com"
print("senai@gmail.com" in email )

if "senai@gmail.com" in email: 
    print("O e-mail é ", email) 
else: 
    print("Não existe")

# texto = 'Python é uma linguagem de programação. Python é simples. Python é organizado. Python é uma excelente linguagem.'
print(texto.count('é'))
print(texto.find('Python', 25,50))

print(texto.rfind('lingua'))
print(texto.index('é'))
print(texto.rindex('é'))

texto = 'Olá Mundo!'
print(texto)
texto_centro = texto.center(150)
texto_centro_2 = texto.center(20,'*')
texto_esquerda = texto.ljust(10)
texto_direita = texto.rjust(150)
print(texto_direita)
print(f'{texto_esquerda}*{texto_direita}')

# Exercício 1: Escreva um programa que verifique se a palavra "python" está presente na string "Estou aprendendo Python".

aprendendo = "Estou aprendendo Python"
if "Python" in aprendendo:
    print("A palavra 'Python' está presente na string 'Estou aprendendo Python'\n")

# exercício 2: Escreva um programa que peça ao usuário para digitar seu nome e verifique se o nome começa com a letra "A" (maiúscula ou minúscula usando .lower).

nome = input("Digite o seu nome:\n")
if nome.startswith ("a"):  
    print("O nome começa com a letra a ou A")
else:
     print("O nome não começa com a letra a ou A")

# Exercício 3: Escreva um programa que peça ao usuário para digitar uma senha e verifique se a senha contém pelo menos 8 caracteres.

senha = input("Digite sua senha aqui:\n")
if len(senha) == 8: 
    print("Essa senha possui 8 caracteres")
else:
    print("Essa senha não possui 8 caracteres")

# Exercício 4: Escreva um programa que peça ao usuário para digitar um número e verifique se o número é uma representação numérica (não contém letras ou símbolos).

numero = input("Digite um número:\n")
if numero.isnumeric():
   print("A string contém apenas dígitos numéricos.")
else:
   print("A string não contém apenas dígitos numéricos.")

# Exercício 5: Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vezes a letra "a" (maiúscula ou minúscula) aparece na frase.

frase = input("Digite uma frase:\n")
contagem = frase.count('a')
print(contagem)  

