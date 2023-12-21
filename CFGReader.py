"""
About: Given CFG:  S→aS |bB|cC 
            B→bB | aC |λ
            C→aS |λ

A program to determine whether an input string is accepted or rejected by the grammar.
"""
def stateS(letter):
    print(letter)
    match letter:
        case "a":
            return "s"
        case "b":
            return "b"
        case "c":
            return "c"
        case _:
            return 'e'

def stateB(letter):
    print(letter)
    match letter:
        case "b":
            return "b"
        case "a":
            return "c"
        case "$":
            return "$"
        case _:
            return 'e'
        
def stateC(letter):
    print(letter)
    match letter:
        case "a":
            return "s"
        case "$":
            return "$"
        case _:
            return 'e'


def main():
    word1 = "abbbcaaa$" #Rejected
    word2 = "ccccbbb$" #Rejected
    word3 = "aabbaac$" #Rejected

    current_word = word3
    state = stateS(current_word[0])
    remain_result = current_word.replace(current_word[0], "", 1)
    isWord = "Rejected"
    for letter in remain_result:
        print("I am in this state: " + letter)
        match state:
            case "s":
                state = stateS(letter)
            case "b":
                state = stateB(letter)
                if state == "$":
                    isWord = "Accepted"
                    break
            case "c":
                state = stateC(letter)
                if state == "$":
                    isWord = "Accepted"
                    break
            case "$":
                print(" I have entered")
                isWord = True
                break
            case "e":
                break
    print("The input string is " + isWord + " by the grammer")


if __name__ == "__main__":
    main()

    