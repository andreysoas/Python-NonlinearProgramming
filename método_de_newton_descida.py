# -*- coding: utf-8 -*-
"""Método de Newton  - Descida.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i8oGn8Y0MPty64W6Y0oJ3WPcJq89NW82
"""

import numpy as np
from sympy import *
from sympy import Lambda
x,y,z,f,a = symbols('x y z f a')

def NewtonDown(funcaoStr:str, x_0:list, EPSILON:float):
  variablesList = [x,y]
  NULLVECTOR = [0,0]
  numVar = len(x_0)
  K=0

  if numVar == 3:
    variablesList.append(z)
    NULLVECTOR.append(0)

  variablesList = tuple(variablesList)
  funcao = Lambda(variablesList,funcaoStr)
  listaDerivadas = []
  
  for i in variablesList:
    f = Lambda(variablesList , diff(funcaoStr,i )) ##Criação da fi
    listaDerivadas.append(f)

  x_0 = np.array(x_0)
  Hessian = []

  for i in listaDerivadas:
    for j in variablesList:
      if numVar == 2:
        Hessian.append(Lambda((x,y),diff(i(x,y),j)))
      else:
        Hessian.append(Lambda((x,y,z),diff(i(x,y,z),j)))
  

  while True:

    #print('Ponto: ',x_0)

    gradient = []
    for i in listaDerivadas:
      if numVar == 2:
        gradient.append(i(x_0[0],x_0[1]))
      else:
        gradient.append(i(x_0[0],x_0[1],x_0[2]))
  
    
    error=0
    for i in gradient:
      error+=i*i
    #print('Gradiente; ',gradient,'\n')
    if (gradient != NULLVECTOR) and (error > EPSILON) :
      
      K+=1
      Hessiana = []
      
      for i in Hessian:
        if numVar == 2:
          Hessiana.append(i(x_0[0],x_0[1]))
        else:
          Hessiana.append(i(x_0[0],x_0[1],x_0[2]))

      Hessiana = np.array(Hessiana,dtype='float').reshape(numVar,numVar)
      Hessiana=np.linalg.inv(Hessiana)
 
      distance = -1*np.dot(Hessiana,gradient)
      #print(distance)
      x_0 = x_0 + distance

    else:
      funcVal = 0
      if numVar == 2:
        funcVal = funcao(x_0[0],x_0[1])
      else:
        funcVal = funcao(x_0[0],x_0[1],x_0[2])

      print('Gradiente: ',gradient)
      print('ITERAÇÃO: ',K,'| Ponto encontrado: ',x_0,' | Valor de função: ',funcVal)
      break

def programInterface():
  
  pInicial=[]
  numVar = 2

  funcao = str(input('Defina a função desejada("end" para terminar): '))
  if funcao == 'end':
    return true

  if 'z' in funcao:
    numVar=3

  for i in range(numVar):
    x = float(input('Coordenada do ponto(uma coordenada por vez): '))
    pInicial.append(x)

  EPSILON = float(input('Erro(ex.: 0.001 , 0.0001 , ...): '))
  
  NewtonDown(funcao,pInicial,EPSILON)
  print('\n')

while True:
  if programInterface():
    break