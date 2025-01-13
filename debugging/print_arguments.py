#!/usr/bin/python3
import sys

print(f"Nom du script : {sys.argv[0]}")
if len(sys.argv) > 1:
    print("Arguments :")
    for i in rnage(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")
else:
    print("Aucun argmuent fourni.")
