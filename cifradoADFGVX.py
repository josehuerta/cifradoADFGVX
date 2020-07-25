class cifradoADFGVX():

    def __init__(self):
        self.matriz=[]
        self.llenarMatriz()

    def llenarMatriz(self):
        self.matriz=[["J","O","5","P","9","G"],
                    ["V","0","V","K","T","8"],
                    ["Y","A","S","2","U","X"],
                    ["W","Z","I","L","C","4"],
                    ["6","N","Q","D","1","E"],
                    ["H","R","3","M","F","7"]]


    def getMatriz(self):
        return self.matriz

    def cifrarMensajeSustitucion(self,msg):
        msg=msg.upper()
        msg_cifrado=[]
        list_adfgvx=["A","D","F","G","V","X"]
        
        len_msg=len(msg)
        for i in range(0,len_msg):#letra del mensaje
            for j in range(0,len(list_adfgvx)):#posicion de columna
                for k in range(0,len(list_adfgvx)):#posicion de fila
                    if msg[i]==self.getMatriz()[j][k]:
                        letra_cifrada=list_adfgvx[j]+list_adfgvx[k]
                        msg_cifrado.append(letra_cifrada)

        return msg_cifrado
    
    def cifrarMensajeTransposicion(self,msg_cifrado,clave):
        msg_cifrado="".join(msg_cifrado)
        msg_cifrado=list(msg_cifrado)
        len_msg_cifrado=len(msg_cifrado)
        len_clave=len(clave)
        matriz_cifrado=[]
        
        #rellenando espacios vacios
        if len_msg_cifrado%len_clave!=0:
            resto=len_msg_cifrado%len_clave
            while resto>=0:
                msg_cifrado.append(" ")
                resto=resto-1
        lista_aux=[]
        #creando la matriz de cifrado
        for i in range(0,len(msg_cifrado)):
            lista_aux.append(msg_cifrado[i])  
            
            if (((i+1)%len_clave)==0) or i==(len(msg_cifrado)-1):
                matriz_cifrado.append(lista_aux)
                lista_aux=[]
        print(clave) 
        self.imprimirMatriz(matriz_cifrado)
        clave_con_poscision=[]
        for i in range(0,len_clave):
            aux=[clave[i],i]
            clave_con_poscision.append(aux)
        
        #ordenamos de forma alfabetica la clave
        clave_ordenada=sorted(clave_con_poscision)
        print(clave_ordenada)
        posicion=[pos for valor,pos in clave_ordenada]

        #ordenando de forma alfabetica la matriz de cifrado
        matriz_columnas_ordenadas=[]
        for i in range(0,len(matriz_cifrado)):
            lista_aux=[]
            for j in posicion:
                lista_aux.append(matriz_cifrado[i][j])
            
            matriz_columnas_ordenadas.append(lista_aux)

        return matriz_columnas_ordenadas
        
    def imprimirMatriz(self,matriz):
        len_matriz=len(matriz)
        for i in range(0,len_matriz):
            print(matriz[i])
        print("\n\n")
    
  
obj=cifradoADFGVX()
msg="todos los domingos vienen a las 7pm"
clave="mouse"
msg_cifrado_sustitucion=obj.cifrarMensajeSustitucion(msg)
print(msg_cifrado_sustitucion)
msg_cifrado_transpuesto=obj.cifrarMensajeTransposicion(msg_cifrado_sustitucion,clave)
obj.imprimirMatriz(msg_cifrado_transpuesto)

print(msg_cifrado_transpuesto)

