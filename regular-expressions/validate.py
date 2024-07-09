import re

email = input("Digite seu e-mail: ").strip()

"""
usuario, dominio = email.split("@")

if usuario and dominio.endswith(".edu"):
    print("Válido")
else:
    print("Inválido")
"""

# re.search(padrão, string, flag=0)
if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):  # r" para raw string - interpreta o \ de maneira usual
    print("Válido")
else:
    print("Inválido")

"""
. -> qualquer caractere exceto nova linha
* -> 0 ou mais repetições
+ -> 1 ou mais repetições
? -> 0 ou 1 repetições - significa opcional
{m} -> m repetições
{m,n} -> m-n repetições
^ -> corresponde ao início da string - NÃO FUNCIONOU
$ -> corresponde ao final da string ou logo antes da nova linha ao final da string - NÃO FUNCIONOU
[] -> conjunto de caracteres
[^] -> exceção ao conjunto
\w word caractere (A-Z, 0-9 e _)
A | B -> A ou B
(...) -> grupo
(?:...) -> versão não capturada 
"""
