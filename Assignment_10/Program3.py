def Factorial(Value):
    iSum = 1

    for i in range(1, Value + 1):
        iSum = iSum * i

    return iSum

def main():
    No = 0
    Result = 0 

    print("Enter the Number : ")
    No = int(input())

    Result = Factorial(No)

    print("The Factorial of Number is :", Result)

if __name__ == "__main__":
    main()