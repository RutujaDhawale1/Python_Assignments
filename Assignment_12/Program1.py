def ChkVowel(str):

    if((str == "a") | (str == "e") | (str == "i") | (str == "o") | (str == "u")):
        return True

    else:
        return False

def main():
    Result = False

    print("Enter the Character :")
    str = input()

    Result = ChkVowel(str)

    if(Result == True):
        print("the alphabet is a Vowel")

    else:
        print("The alphabet is not a vowel")

if __name__ == "__main__":
    main()  