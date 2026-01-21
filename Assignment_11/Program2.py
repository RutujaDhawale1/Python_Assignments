def CountDigits(Value):
    iCnt = 0

    while(Value != 0):

        Value = Value // 10
        iCnt = iCnt + 1

    return iCnt

def main():
    Result = 0

    print("Enter the numbre:")
    No = int(input())

    Result = CountDigits(No) 

    print("the Count of Digits is :", Result)


if __name__ == "__main__":
    main()    