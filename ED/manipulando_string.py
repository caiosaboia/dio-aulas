string = "oLá"

print(string.upper())
# -> OLÁ

print(string.lower())
# -> olá

print(string.title())
# -> Olá


frase = "   frase "


print(frase.strip())

print(frase.lstrip())

print(frase.rstrip())

print(frase.rstrip().lstrip().center(15, "#"))

print(".".join(frase))

# Testando formart e fstring
nome = "Caio"
idade = 21
profissao = "pesquisador"
linguagem = "python"
saldo = 2223.4442

dados = {"name": "Guilherme", "idade": 21, "saldo": 2223}


print("Nome: %s Idade: %s" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(nome, idade))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(name=nome, age=idade))

print("Nome: {name} Idade: {idade}".format(**dados))


print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:1.5f}")


# Fatiamente
nomes = "Caio Joao Neto"
print(nomes[0])
print(nomes[:5])
print(nomes[5:])
print(nomes[9:13])
print(nomes[10:16:2])
print(nomes[:])
print(nomes[::-1])

# String Multiplas Linhas

mensagem = f""" 
Olá meu nome é {nome},
e esse é um teste de string de Multiplas
linhas.
    """

print(mensagem)
