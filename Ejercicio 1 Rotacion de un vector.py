import numpy as np

def rot_z(x,y,z,angulo):
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

def rot_x(x,y,z,angulo):
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

def rot_y(x,y,z,angulo):
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

def rotar():
    '''
    Este bloque de codigo sirve para introducir valores y imprimir en pantalla tambien 
    combierte los angulos a radiantes con la funcion deg2rad de numpy
    no tiene parametros de salida ni entrada 
    '''
    x = float(input("introdusca el valor de X: "))
    y = float(input("introdusca el valor de Y: "))
    z = float(input("introdusca el valor de Z: "))
    eje = int(input("introdusca el valor del eje a rotar(eje x = 1,eje y = 2,eje z = 3): "))
    angulo = np.deg2rad(float(input("introdusca el valor de el angulo: ")))

    if(eje == 1):
        print(rot_x(x,y,z,angulo))
    elif(eje == 2):
        print(rot_y(x,y,z,angulo))
    else:
         print(rot_z(x,y,z,angulo))

rotar()