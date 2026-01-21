def ChkDiv(Value):

    if(((Value % 3)== 0) and ((Value % 5) == 0)):
        return True

    else:
        return False


def main():
    No = 0
    Result = False

    print("Enter The Number:")
    No = int(input())

    Result = ChkDiv(No)

    if(Result == True):
        print(No,"is Divisible by 3 and 5")

    else:
        print(No," is Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()


