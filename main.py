from my_operations import add, diff, mul
from greeting_a import greeting_a
from greeting_b import greeting_b
from greeting_c import greeting_c
def main():

    num1 = int(input("Enter your number 1:"))
    num2 = int(input("Enter your number 2:"))
    
    diff(num1, num2)

    # Member A call method add() at line: 8
    # Member B call method diff() at line: 8
    # Member C call method mul() at line: 8
    
    pass

if __name__ == "__main__":
    main()