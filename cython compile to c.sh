cython --embed -o my_code.c my_code.py
gcc -o my_code my_code.c -I /usr/include/python3.8 -lpython3.8
