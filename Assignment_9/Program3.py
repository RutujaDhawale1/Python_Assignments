def SquareNum(Value):
    Ans = 0
    Ans = Value * Value
    return Ans

def main():
    No = 0
    Result = 0

    print("Enter the number : ")
    No = int(input())

    Result = SquareNum(No)

    print("The Square of", No , "is : ", Result)

if __name__ == "__main__":
    main()
