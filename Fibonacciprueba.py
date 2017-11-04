import sys
import numpy


def fib(n):
    i=2
    fn0=0
    fn1=1
    global fn
    fn=fn0+fn1

    
    while(i<n):
       fn0=fn1
       fn1=fn
       fn=fn0+fn1
       i=i+1

    global s
    s= "Posicion del numero ingresado (n) en serie de Fibonacci es: "+ str(fn)
    #print s

def fib_anterior(n):
    i=2
    fn0=0
    fn1=1
    global fna
    fna=fn0+fn1

    while(i<n-1):
       fn0=fn1
       fn1=fna
       fna=fn0+fn1
       i=i+1

    global sa
    sa= "Posicion anterior del numero ingresado (n-1) en serie de Fibonacci es: "+ str(fna)
    #print s    




n=input("Ingrese un numero natural\n")

    
fib(n)
fib_anterior(n)
print s
print sa
