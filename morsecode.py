# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()
    counter = 0
    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"
    return message


def is_help_command(user_input):
    return user_input.lower()=='h' or user_input.lower()=="help"


def is_validated_english_sentence(user_input):
    user_input = user_input.replace(",", "")
    user_input = user_input.replace(".", "")
    user_input = user_input.replace("!", "")
    user_input = user_input.replace("?", "")
    user_input = user_input.replace(" ", "")
    return user_input.isalpha()


def is_validated_morse_code(user_input):
    morse_code = get_morse_code_dict()
    user_list = user_input.split(' ')
    for i in user_list:
        if(i==''):
            continue
        if i not in morse_code.values():
            return False
    return True


def get_cleaned_english_sentence(raw_english_sentence):
    raw_english_sentence = raw_english_sentence.replace(".","")
    raw_english_sentence = raw_english_sentence.replace(",","")
    raw_english_sentence = raw_english_sentence.replace("!","")
    raw_english_sentence = raw_english_sentence.replace("?","")
    raw_english_sentence = raw_english_sentence.lstrip(" ")
    raw_english_sentence = raw_english_sentence.rstrip(" ")
    return raw_english_sentence

def decoding_character(morse_character):
    morse_code = get_morse_code_dict()
    for i in morse_code:
        if(morse_character==morse_code[i]):
            return i

def encoding_character(english_character):
    morse_code = get_morse_code_dict()
    return morse_code[english_character]

def decoding_sentence(morse_sentence):
    morse_list = morse_sentence.split(' ')
    ans=""
    for i in morse_list:
        if(i==''):
            ans+=' '
        else:
            ans +=(decoding_character(i))
        # ans = "#".join(decoding_character(i))
    return ans

def encoding_sentence(english_sentence):
    english_sentence = get_cleaned_english_sentence(english_sentence)
    english_sentence = english_sentence.upper()
    english_list = english_sentence.split(' ')
    ans=""
    for i in english_list:
        if(i==''):
            continue
        for l in range(len(i)):
            # ans=" ".join(encoding_character(i[l]))
            ans+=encoding_character(i[l])
            ans+=' '
        ans+=" "
    ans = ans.rstrip(" ")
    return ans

def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    while(True):
        user_input = input("Input your message(H - Help, 0 - Exit) :")
        if(user_input=='0'):
            break
        if(is_help_command(user_input)):
            print(get_help_message())
            continue
        if(is_validated_english_sentence(user_input)):
            print(encoding_sentence(user_input))
        elif(is_validated_morse_code(user_input)):
            print(decoding_sentence(user_input))
        else:
            print("Wrong Input")
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
