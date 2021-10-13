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
# print_number(3)

number = 5
char_code = 32 + 16 + number
print(f'symbol: {chr(char_code)}')