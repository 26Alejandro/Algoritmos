
def buscar_error(tree):
    tamano=len(tree)
    n = len(tree)+1
    tamaño_de_trabajo_0= n/2
    for i in range(tamano-2):
       if  tree[i]== tree[i*2+1]+tree[i*2+2]:
           continue
       else:
           print('el error esta en : ', i)
        
    
    
    



lista= [29, 13, 16, 5, 8, 9, 1]
#       0   1  1    2  2  2  2
# (1,10)

buscar_error(lista)
