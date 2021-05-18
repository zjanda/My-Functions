from utils import reverseStr
from utils import div

letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
               23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]


def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def emoji_converter(message):
    emojis = {
        ":)": "🙂",
        ":(": "🙁",
        ":'(": "😢",
        ";(": "😢",
        ";)": "😉",
        ":P": "😋",
        ":D": "😃",
        ":S": "🥴"
    }
    words = message.split(' ')

    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '

    return output


def decimal_to_x_base(number: int, new_base: int):
    remainder_list = []

    while number >= new_base:
        remainder_digit = number % new_base
        if remainder_digit >= 10:
            remainder_list.append(convert_to_letter(remainder_digit))
        else:
            remainder_list.append(str(remainder_digit))
        number = int(number / new_base)  # type casted to truncate any decimals

    if number >= 10:
        number = convert_to_letter(number)
    remainder_list.append(str(number))

    return reverseStr(''.join(remainder_list))


def convert_to_letter(number: int):
    return letter_list[number_list.index(int(number))]


def convert_to_num(letter: str):
    return number_list[letter_list.index(str(letter))]


def x_base_to_decimal(number: int, original_base: int):
    x: str
    num_list = []
    for x in str(number):
        num_list.append(x)
    sumValue = 0
    for digit in num_list:
        if digit in letter_list:
            digit = convert_to_num(digit)
        sumValue = int(digit) + original_base * sumValue
    return sumValue


def to_binary(number: int, original_base: int = 10):
    return decimal_to_x_base(x_base_to_decimal(number, original_base), 2)


def to_octal(number: int, original_base: int):
    return decimal_to_x_base(x_base_to_decimal(number, original_base), 8)


def to_hexidecimal(number: int, original_base: int):
    return decimal_to_x_base(x_base_to_decimal(number, original_base), 16)


int_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
            23, 24, 25, 26]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Using the above Alpha <-> Integer relations, where a = 01, and z = 26, etc. the following functions convert strings
# of letters to strings of integers
def text_2_num(word: str):
    return_list = []
    for letter in word:
        return_list.append(int_list[alphabet.index(letter.lower())])

    for x in return_list:
        return_list[return_list.index(x)] = str(x)

    return_list = ''.join(return_list)

    return {'int': int(return_list), 'str': return_list}


def num_2_text(num: int):
    backward = []
    while num != 0:
        backward.append(alphabet[num % 100 - 1])
        num = div(num, 100, False)

    backward.reverse()
    return ''.join(backward)
