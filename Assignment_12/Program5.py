def PrintNumber(Value):

    for i in range(Value,0,-1):

        print(i)
        

def main():

    print("Enter the Number : ")
    No = int(input())

    PrintNumber(No)


if __name__ == "__main__":
    main()