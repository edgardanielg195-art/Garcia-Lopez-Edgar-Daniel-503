import numpy as np

def Rz(x,y,z,angulo):
    '''
    Este bloque de codigo para calcular la matriz de rotacion de Z 
    recibe los parametros valor de X, valor de Y, valor de Z y el valor del angulo 
    los parametros de salida es un vector resultado de la multiplicacion de la matriz 
    de rotacion de Z por el array conformado por (X,Y,Z)
    '''
    arr1 = np.array([[np.cos(angulo), -np.sin(angulo), 0],
                     [np.sin(angulo), np.cos(angulo), 0],
                     [0, 0, 1]])
    arr2 = np.array([x,y,z])
    return arr1 @ arr2

def Rx(x,y,z,angulo):
    '''
    Este bloque de codigo para calcular la matriz de rotacion de X 
    recibe los parametros valor de X, valor de Y, valor de Z y el valor del angulo 
    los parametros de salida es un vector resultado de la multiplicacion de la matriz 
    de rotacion de X por el array conformado por (X,Y,Z)
    '''
    arr1 = np.array([[1, 0, 0],
                     [0,np.cos(angulo), -np.sin(angulo)],
                     [0, np.sin(angulo), np.cos(angulo)]])
    arr2 = np.array([x,y,z])
    return arr1 @ arr2

def Ry(x,y,z,angulo):
    '''
    Este bloque de codigo para calcular la matriz de rotacion de Y 
    recibe los parametros valor de X, valor de Y, valor de Z y el valor del angulo 
    los parametros de salida es un vector resultado de la multiplicacion de la matriz 
    de rotacion de Y por el array conformado por (X,Y,Z)
    '''
    arr1 = np.array([[np.cos(angulo), 0,np.sin(angulo)],
                     [0,1,0],
                     [-np.sin(angulo),0, np.cos(angulo)]])
    arr2 = np.array([x,y,z])
    return arr1 @ arr2

def main():
    '''
    Este bloque de codigo sirve para introducir valores y imprimir en pantalla tambien 
    combierte los angulos a radiantes con la funcion 
    no tiene parametros de salida ni entrada deg2rad de numpy
    '''
    x = float(input("introdusca el valor de X: "))
    y = float(input("introdusca el valor de Y: "))
    z = float(input("introdusca el valor de Z: "))
    eje = int(input("introdusca el valor del eje a rotar: "))
    angulo = np.deg2rad(float(input("introdusca el valor de el angulo: ")))

    if(eje == 1):
        print(Rx(x,y,z,angulo))
    elif(eje == 2):
        print(Ry(x,y,z,angulo))
    else:
         print(Rz(x,y,z,angulo))
         print(type(Rz(x,y,z,angulo)))

main()