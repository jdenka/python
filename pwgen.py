import random
import string

letters = string.ascii_letters
num = string.digits
pleb = '!@^*$'
all = letters + num + pleb

def main():
    print("Skriv in pin eller pw")
    pwellerkod = input("pin eller pw? ")
    if pwellerkod == "pin":
        manga = int(input("Hur många pinkoder? "))
        for p in range(manga):
            pin = ''
            for c in range(4):
                pin += random.choice(num)
            print(pin)
    elif pwellerkod == "pw":
        len = int(input("Lösenordslängd? "))
        many = int(input("Hur många lösenord? "))
        for p in range(many):
            password = ''
            for c in range(len):
                password += random.choice(all)
            print(password)
    else: 
        print("Gör om gör rätt!")
        main()
main()
