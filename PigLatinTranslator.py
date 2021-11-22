#Tom Lazore
#Lab 8 Pig Latin Translator
#This program colletcts input from user and translate their sentence into Pig Latin

def main():

    print("Type a sentence and this program will translate it into Pig Latin")
    print()
    sentence = str(input("English sentence: ")).split()
    print()
    print("Pig Latin translation:")
    for i in sentence:
        print(i[1:] + i[0] + "ay", end = " ")
    print()


main()


