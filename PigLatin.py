__author__ = 'zacharypinto and liamglynn'


def trans(word):
    letter = word[0]
    ending = "ay"
    root = word[1:]
    newWord = root + letter + ending
    return newWord

#intro
print("Welcome To The Pig Latin Translator!")
repeat = True

while repeat:
    origSent = input("\nInput a sentence to be translated into Pig Latin: ").lower()

    string = ""
    punc = ""

    if origSent[len(origSent) - 1] == "." or origSent[len(origSent) - 1] == "!" or origSent[len(origSent) - 1] == "?":
        string = origSent[0:len(origSent) - 1]
        punc = origSent[len(origSent) - 1]

    else:
        string = origSent


    listSent = string.split()

    newSent = "\n"

    for item in listSent:
        if item == listSent[0]:
            newSent += trans(item).capitalize() + " "
        elif item == listSent[len(listSent) - 1]:
            newSent += trans(item)
        else:
            newSent += trans(item) + " "

    newSent += punc

    print(newSent + "\n")

    answer = input("Would you like to translate another sentence? ").upper()

    if answer == "yes".upper():
        repeat = True

    else:
        repeat = False
        print("\nThank you for translating")
