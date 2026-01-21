def Even(Value):

    for i in range(2, Value + 1, 2):
        print(i)

def main():
    print("Enter the Number : ")
    No = int(input())

    Even(No)

if __name__ == "__main__":
    main()    
