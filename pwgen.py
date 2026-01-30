import secrets
import string

LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?"
ALL_CHARS = LETTERS + DIGITS + SPECIAL


def generate_pin(length: int = 4) -> str:
    return ''.join(secrets.choice(DIGITS) for _ in range(length))


def generate_password(length: int) -> str:
    # Ensure at least one of each type
    password = [
        secrets.choice(LETTERS),
        secrets.choice(DIGITS),
        secrets.choice(SPECIAL)
    ]
    # Fill the rest
    password += [secrets.choice(ALL_CHARS) for _ in range(length - 3)]
    # Shuffle the order
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def main():
    while True:
        choice = input("pin or pw? (q to quit): ").strip().lower()
        
        if choice == "q":
            break
        elif choice == "pin":
            count = int(input("How many PIN codes? "))
            for _ in range(count):
                print(generate_pin())
        elif choice == "pw":
            pw_length = int(input("Password length (minimum 12): "))
            if pw_length < 12:
                print("Warning: Passwords under 12 characters are insecure")
                continue
            count = int(input("How many passwords? "))
            for _ in range(count):
                print(generate_password(pw_length))
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
