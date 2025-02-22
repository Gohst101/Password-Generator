import string
import secrets


def prompt_bool(prompt, default=True):
    default_str = "y" if default else "n"
    response = input(f"{prompt} [y/n] (default: {default_str}): ").strip().lower()
    if response == "":
        return default
    return response.startswith('y')


def main():
    try:
        length = int(input("Enter password length (5-300): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return


    if length < 5 or length > 300:
        print("Password length must be between 5 and 300.")
        return


    include_upper = prompt_bool("Include uppercase letters?", default=True)
    include_lower = prompt_bool("Include lowercase letters?", default=True)
    include_digits = prompt_bool("Include digits?", default=True)
    include_punct = prompt_bool("Include punctuation?", default=True)

    if not (include_upper or include_lower or include_digits or include_punct):
        print("At least one character set must be selected!")
        return


    characters = ""
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_punct:
        characters += string.punctuation


    full_password = "".join(secrets.choice(characters) for _ in range(length))


    print("\nGenerated Password:")
    print(full_password)


if __name__ == "__main__":
    main()