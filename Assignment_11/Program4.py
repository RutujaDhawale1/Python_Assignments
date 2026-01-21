def ReverseNum(Value):

    iRev = 0

    while(Value != 0):
        iDigit = Value % 10
        iRev = (iRev * 10) + iDigit
        Value = Value // 10

    return iRev

def main():
    Result = 0

    print("Enter the Number")
    No = int(input())

    Result = ReverseNum(No)

    print("The Reverse No is :", Result)

if __name__ == "__main__":
    main()        
