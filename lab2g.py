#!/usr/bin/env python3

#Author: Ralph Louisse Tolentino
#Author ID: 153087226
#Date Created: 2025/02/02"

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')
