import codebug_tether
import random

codebug = codebug_tether.CodeBug()


def print_zero():
    codebug.clear()
    codebug.set_row(4, 0b00100)
    codebug.set_row(3, 0b01010)
    codebug.set_row(2, 0b01010)
    codebug.set_row(1, 0b01010)
    codebug.set_row(0, 0b00100)

def print_one():
    codebug.clear()
    codebug.set_row(4, 0b00100)
    codebug.set_row(3, 0b10100)
    codebug.set_row(2, 0b00100)
    codebug.set_row(1, 0b00100)
    codebug.set_row(0, 0b00100)

def print_five():
    codebug.clear()
    codebug.set_row(4, 0b01110)
    codebug.set_row(3, 0b01000)
    codebug.set_row(2, 0b01110)
    codebug.set_row(1, 0b00010)
    codebug.set_row(0, 0b01110)


def print_three():
    codebug.clear()
    codebug.set_row(4, 0b01110)
    codebug.set_row(3, 0b00010)
    codebug.set_row(2, 0b01110)
    codebug.set_row(1, 0b00010)
    codebug.set_row(0, 0b01110)


def print_six():
    codebug.clear()
    codebug.set_row(4, 0b00100)
    codebug.set_row(3, 0b01000)
    codebug.set_row(2, 0b01110)
    codebug.set_row(1, 0b01010)
    codebug.set_row(0, 0b00100)


def print_two():  
    codebug.clear()
    codebug.set_row(4, 0b01110)
    codebug.set_row(3, 0b10011)
    codebug.set_row(2, 0b00110)
    codebug.set_row(1, 0b01100)
    codebug.set_row(0, 0b11111)


def print_four():
    codebug.clear()
    codebug.set_row(4, 0b1010)
    codebug.set_row(3, 0b1010)
    codebug.set_row(2, 0b1110)
    codebug.set_row(1, 0b0010)
    codebug.set_row(0, 0b0010)
   

def print_seven():
    codebug.clear()
    codebug.set_row(4, 0b11111)
    codebug.set_row(3, 0b00010)
    codebug.set_row(2, 0b00100)
    codebug.set_row(1, 0b01000)
    codebug.set_row(0, 0b10000)


def print_eight():
    codebug.clear()
    codebug.set_row(4, 0b01110)
    codebug.set_row(3, 0b01010)
    codebug.set_row(2, 0b01110)
    codebug.set_row(1, 0b01010)
    codebug.set_row(0, 0b01110)


def print_nine():
    codebug.clear
    codebug.set_row(4, 0b01110)
    codebug.set_row(3, 0b10011)
    codebug.set_row(2, 0b01110)
    codebug.set_row(1, 0b01100)
    codebug.set_row(0, 0b11000)


def main():
    # number = 
    


main()