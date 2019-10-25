#!/bin/python3

answer = "0aea5ceb227330e6d506b6fa61aef1d20d0959a8ed52057a6e005c6bd4995461"

from hashlib import sha256

for i in range(0, 1000000):
    if sha256(str(i).zfill(6).encode()).hexdigest() == answer:
        print(f"Pin is: {i}") 
        break
