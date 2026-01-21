def ChkPrime(Value):

    for i in range(2,int(Value/2) + 1):

        if(Value % i == 0):
            
            return False

    return True

def main():
    No = 0
    Result = False

    print("Enter the Number :")
    No = int(input())

    Result = ChkPrime(No)

    if(Result == True):

        print(No,"is Prime Number")

    else:
        print(No,"is Not a Prime Number")

if __name__ == "__main__":
    main()

