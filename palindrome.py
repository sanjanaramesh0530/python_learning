def is_palindrome(text: str) -> bool:
    normalized = "".join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]


if __name__ == "__main__":
    text = input("Enter text: ").strip()
    if is_palindrome(text):
        print("Palindrome")
    else:
        print("Not a palindrome")
