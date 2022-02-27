nome = input("Nome da classe: ")
qtd = int(input("Quantidade de atributos: "))
p = input("public, private ou protected: ")
atributos = []
uppernome = nome.upper()+"_H"
lowernome = nome.lower()+".h"
for i in range(qtd):
  a = []
  a.append(input("Atributo: "))
  a.append(input("Tipo: "))
  atributos.append(a)
print("\nGerando...\n\nClasse completa -\n")
print("class",nome+"{","\n\t"+p+":")
for j in atributos:
  print("\t"+j[1],j[0]+";")
print("\tpublic:")
print("\t"+nome+"(){")
for j in atributos:
  if (j[1] == "int") or (j[1] == "float"):
    c = "0"
  else:
    c = '""'
  print("\t\tthis->"+j[0],"=",c+";")
print("\t}")
arguments = ""
for j in atributos:
  arg = j[1]+" "+j[0]
  arguments = arguments+arg+""
  arguments = arguments+","
arguments = arguments.rstrip(arguments[-1])
print("\t"+nome+"("+arguments+"){")
for j in atributos:
  print("\t\tthis->"+j[0],"=",j[0]+";")
print("\t}")
for j in atributos:
  print("\t"+j[1],"get"+j[0].capitalize()+"(){\n\t\treturn",j[0]+";\n\t}")
  print("\tvoid set"+j[0].capitalize()+"("+j[1],j[0]+"){\n\t\tthis->"+j[0],"=",j[0]+";\n\t}")
print("};")
#
#
#.h agora
#
#
print("\n\n\nClasse cabeçalho -\n")
print("#ifndef",uppernome)
print("#define",uppernome,"\n")
print("#include<iostream>\nusing namespace std;")
print("class",nome+"{","\n\t"+p+":")
for j in atributos:
  print("\t"+j[1],j[0]+";")
print("\tpublic:")
print("\t"+nome+"();")
arguments = ""
for j in atributos:
  arg = j[1]+" "+j[0]
  arguments = arguments+arg+""
  arguments = arguments+","
arguments = arguments.rstrip(arguments[-1])
print("\t"+nome+"("+arguments+");")
for j in atributos:
  print("\t"+j[1],"get"+j[0].capitalize()+"();")
  print("\tvoid set"+j[0].capitalize()+"("+j[1],j[0]+");")
print("};")
print("\n#endif // !"+uppernome)
#
#
#.o agora
#
#
print("\n\n\nMétodos fora do cabeçalho -\n\n")
print('#include<iostream>\n#include"'+lowernome+'"\nusing namespace std;\n')
print(nome+"::"+nome+"(){")
for j in atributos:
  if (j[1] == "int") or (j[1] == "float"):
    c = "0"
  else:
    c = '""'
  print("\tthis->"+j[0],"=",c+";")
print("}")
arguments = ""
for j in atributos:
  arg = j[1]+" "+j[0]
  arguments = arguments+arg+""
  arguments = arguments+","
arguments = arguments.rstrip(arguments[-1])
print(nome+"::"+nome+"("+arguments+"){")
for j in atributos:
  print("\tthis->"+j[0],"=",j[0]+";")
print("}")
for j in atributos:
  print(j[1],nome+"::"+"get"+j[0].capitalize()+"(){\n\treturn",j[0]+";\n}")
  print("void",nome+"::"+"set"+j[0].capitalize()+"("+j[1],j[0]+"){\n\tthis->"+j[0],"=",j[0]+";\n}")
