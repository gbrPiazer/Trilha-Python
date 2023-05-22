''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 


   T (1 ≤ |T| ≤ 500)
'''
T = input()
quantidade = T.strip().__len__()

if quantidade <= 140:
    print("TWEET")
else:
    print("MUTE")

print(quantidade)