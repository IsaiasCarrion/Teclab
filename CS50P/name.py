import sys

if len(sys.argv) < 2:
    sys.exit('Muy pocos argunmentos')

for arg in sys.argv:

    print('Hola, mi nombre es ', arg)