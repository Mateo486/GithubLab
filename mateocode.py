
def encode(num):
    result = ""
    num = list(num)

    for item in range(len(num)):
        num[item] = int(num[item])
        if (num[item] + 3) > 10:
            num[item] += 3
            num[item] -= 10
        else:
            num[item] += 3
    for item in range(len(num)):
        result += str(num[item])
    return result







if __name__ == "__main__":
    while True:
        print("""
Menu
-------------
1. Encode
2. Decode
3. Quit
""")

        option = input("Please Enter an option: ")
        password = str(input("Please enter your password to encode: "))

        if option == "1":
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            print(f"The encoded password is {encoded} and the original password is {password}")
        elif option == "3":
            quit()

