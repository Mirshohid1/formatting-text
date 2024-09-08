import sys

def longest_word(text: str) -> str:
    words = text.split()
    all_words = []
    for word in words:
        all_words.extend(word.split(','))

    return max(all_words, key=len)

def add_remove_spaces(text: str):
    index = 0
    while index < len(text):
        if text[index] == ',':
            if text[index-1] == ' ':
                text = text[:index-1] + text[index:]
                index -= 1
            if index + 1 < len(text) and text[index+1] != ' ' and text[index+1] != '\n':
                text = text[:index+1] + ' ' + text[index+1:]
                index += 1
        index += 1

    return text

def formatting_text(text: str):
    len_max_line = len(longest_word(text)) * 3
    text = add_remove_spaces(text)
    index = 0
    result = list(text)

    len_line = 0
    while index < len(text):
        if len_line == len_max_line: # len_line qator oxiriga yetganda ishberadi
            if text[index] != ' ': # agar qator oxiri space bo'lmasa yani sybmol bo'lsa while space gacham teskari index sanaydi va space o'rniga \n qo'yadi
                temp = index
                len_word_left = 0
                len_word_right = 0
                flag = 0
                while text[temp] != ' ':
                    temp -= 1
                    len_word_left+=1
                spare_temp = temp
                while flag == 0:
                    if text[temp] == ' ' or text[temp] == '\n' or text[temp] == '\0' or text[temp] == ',':
                        flag = 1
                    len_word_right += 1
                    temp += 1
                if len_word_left + 1 == len_word_right:
                    result[temp] = '\n'
                else:
                    result[spare_temp] = '\n'
                index = temp
            else: # agar teskarisi yani space bo'lsa uni o'rniga \n qo'yadi
                result[index] = '\n'
            len_line = 0
        len_line+=1
        index += 1
    return ''.join(result)

if len(sys.argv) != 2:
    print("Неправильное количество аргументов.")
else:
    print(formatting_text(str(sys.argv[1])))

# print(formatting_text("once upon a time, in a land far far away lived a princess , whose beauty was yet unmatched"))
# print(formatting_text("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,yandex"))