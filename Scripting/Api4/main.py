"""
1.  Si el número es divisible por 3, se imprimirá en pantalla el mensaje “Fizz”.
2.  Si el número es divisible por 5, se imprimirá en pantalla el mensaje “Buzz”.
3.  Si  el  número es divisible por 3 y por 5, se impimirá en pantalla el mensaje “Fizz Buzz”.
4.  Para el resto de los números que no cumple ninguna de las condiciones anteriores, se mostrará en pantalla el mismo número.
Pista:  Para  evaluar  si  un  número  es  divisible  por  otro, se debe utilizar el operador módulo (%).
"""
for numero in range(1, 101):
  if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
  elif numero % 3 == 0:
    print("Fizz")
  elif numero % 5 == 0:
    print("Buzz")
  else:
    print(numero)