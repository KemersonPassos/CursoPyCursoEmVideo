n = (input("Digite algo: "))
print("O tipo primitivo desse valor é", type(n))

print("Só tem espaços?", n.isspace())
print("É um número?", n.isnumeric())
print("É alfabético?", n.isalpha())
print("É alfanumérico?", n.isalnum())
print("Está em maiúsculas?", n.isupper())
print("Está em minúsculas?", n.islower())
print("Está capitalizada?", n.istitle())
print("É um dígito?", n.isdigit())
print("É um identificador?", n.isidentifier())
print("É imprimível?", n.isprintable())
print("É um email?", "@" in n and "." in n) 


#exercicio "dissecando variaveis" de tipos primitivos e input