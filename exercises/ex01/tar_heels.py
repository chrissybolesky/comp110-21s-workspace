"""An exercise in remainders and boolean logic."""

__author__ = "730135317"


n: int = int(input("Enter an int:"))

x: int = 0
y: int = 0
b: bool = x == y 

if n % 2 == x and n % 7 == y: 
    print("TAR HEELS")
else: 
    if n % 2 == x:
        print("TAR")
    else:
        if n % 7 == y:
            print("HEELS") 
        else: 
            print("CAROLINA") 