# !user/bin/env python3

# Created by: RJ Fromm
# Created on: October 2019
# This program determines if a letter is uppercase or lowercase


def main():

    ch = input("Please Enter a letter (uppercase or lowercase) : ")
    if(ord(ch) >= 65 and ord(ch) <= 90):
        print("The letter", ch, "is an uppercase letter")
    elif(ord(ch) >= 97 and ord(ch) <= 122):
        print("The letter", ch, "is a lowercase letter")
    else:
        print(ch, "is Not a lowercase or Uppercase letter")


if __name__ == "__main__":
    main()
