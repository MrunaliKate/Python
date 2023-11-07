import random

def password_generator(char_length, num_length, symbol_length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0,1,2,3,4,5,6,7,8,9"
    symbols = "!@#$%^&*()"

    selectedChars = random.sample(chars, char_length)
    selectedNums = random.sample(nums, num_length)
    selectedSymbols = random.sample(symbols, symbol_length)

    password_list = selectedChars + selectedNums + selectedSymbols

    random.shuffle(password_list)

    password_str = "".join(password_list)

    return password_str

if __name__ == "__main__":
    char_length = int(input("Enter the Number of the Characters that you need in the password : "))
    num_length = int(input("Enter the Number of the Numbers that you need in the password : "))
    symbol_length = int(input("Enter the Number of the Symbols that you need in the password : "))

    password = password_generator(char_length,num_length, symbol_length)

    print("The Randomly Generated Password is :",password)