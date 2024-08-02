""" 
    Iterando strings com while
"""

nome = 'Cléverson Santana do Nascimento'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'_{letra}'
   
    indice += 1

novo_nome += '_'
print(novo_nome)