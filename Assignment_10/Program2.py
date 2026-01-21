def Sum(Value):
    iSum = 0

    for i in range(1, Value + 1):
        iSum = iSum + i

    return iSum

def main():
    No = 0
    Result = 0

    print("Enter The Number : ")
    No = int(input())

    Result = Sum(No)

    print("Sum of Natural Numbers is :", Result)

if __name__ == "__main__":
    main()
