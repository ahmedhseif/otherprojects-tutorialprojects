import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")

dic = {row.letter: row.code for (index, row) in file.iterrows()}
print(dic)


def generate_phonetic():
    global work
    word = input("Write a word: ").upper()
    try:
        result = [dic[alphabet] for alphabet in word]
    except KeyError:
        print("Please enter only letters")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
