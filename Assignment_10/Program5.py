def OddNum(Value):

    for i in range(1, Value + 1, 2):
        print(i)

def main():

    print("Enter the Number :")
    No = int(input())

    OddNum(No)

if __name__ == "__main__":
    main()