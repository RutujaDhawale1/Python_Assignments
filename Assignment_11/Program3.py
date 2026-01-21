def SumDigits(Value):
    iCnt = 0
    iSum = 0

    while(Value != 0):

        Value = Value // 10
        iCnt = iCnt + 1
        iSum = iSum + iCnt

    return iSum

def main():

    Result = 0

    print("Enter the numbre:")
    No = int(input())

    Result = SumDigits(No) 

    print("the Sum of Digits is :", Result)


if __name__ == "__main__":
    main()    