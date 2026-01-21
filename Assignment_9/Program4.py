def CubeOfNum(Value):
    Ans = 0
    Ans = Value * Value * Value

    return Ans

def main():
    No = 0
    Result = 0

    print("Enter the Number : ")
    No = int(input())

    Result = CubeOfNum(No)

    print("The Cube of",No,"is : ", Result)

if __name__ == "__main__":
    main()

