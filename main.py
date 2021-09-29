import codebug_tether
import random
import time

codebug = codebug_tether.CodeBug()


def read_from_file(path):
    characters = []
    with open(path, 'r') as chars_file:
        for line in chars_file:
            data = []
            datas = line.split(' # ')[0]
            data = datas.split(', ')
            number_data = [int(char, 16) for char in data]
            characters.append(number_data)
    return characters


def print_character(character):
    codebug.clear()
    character.append(0)
    character.insert(0, 0)
    for col_index in range(0, 5):
        codebug.set_col(col_index, character[col_index] >> 3)


def print_number(number):
    charaters = read_from_file('font.txt')
    char_number = charaters[16 + number]
    print_character(char_number)
    

def print_zero():
    codebug.clear()
    codebug.set_row(4, 0x04)
    codebug.set_row(3, 0x0A)
    codebug.set_row(2, 0x0A)
    codebug.set_row(1, 0x0A)
    codebug.set_row(0, 0x04)


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


# def print_number(number):
#     if number == 1:
#         print_one()
#     elif number == 2:
#         print_two()
#     elif number == 3:
#         print_three()
#     elif number == 4:
#         print_four()
#     elif number == 5:
#         print_five()
#     elif number == 6:
#         print_six()
#     elif number == 7:
#         print_seven()
#     elif number == 8:
#         print_eight()
#     elif number == 9:
#         print_nine()
#     elif number == 0:
#         print_zero()


def waiting_for_feedback():
    print('waiting for keypress')
    while True:
        button_A = codebug.get_input('A')
        button_B = codebug.get_input('B')
        if button_A == 1:
            print('A')
            return True
        if button_B == 1:
            print('B')
            return False



def main():
    numbers = []
    for number in range(0, 10):
        numbers.append(number)
    print(numbers)
    while True:
        time.sleep(2)
        random_number = random.randint(0, 9)
        if random_number in numbers:
            print(random_number)
            print_number(random_number)
            if waiting_for_feedback():
                break
            numbers.remove(random_number)
    codebug.clear()
    print('You win!')


# main()
print_number(9)