import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow('Hola ' + sys.argv[1])