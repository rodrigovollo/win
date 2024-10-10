import sys
import subprocess
import os
import string
print('Content-type: text/html \n\n')
print('<h1>foi</h1>')

n = len(sys.argv)
print("Total arguments passed:", n)
# Arguments passed
print("\nName of Python script:", sys.argv[1])
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
comando = sys.argv[1]
print("\ncomando:",comando.strip())
#resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
#print("\n", resultado.stdout)
#resultado = os.system("dir")
print("chegou",comando.strip())
     
# Addition of numbers
#Sum = 0
# Using argparse module
#for i in range(1, n):
 #   Sum += int(sys.argv[i])
     
#print("\n\nResult:", Sum)

