import random

def get_secret_number():
    """Ek random 3-digit ka secret number generate karta hai."""
    digits = list('0123456789')
    random.shuffle(digits)
    return ''.join(digits[:3])

def get_clues(guess, secret_number):
    """Guess ke mutabiq Pico, Fermi, ya Bagels ka clue return karta hai."""
    if guess == secret_number:
        return "You got it!"  # Agar guess sahi ho to message deta hai.

    clues = []
    for i in range(3):
        if guess[i] == secret_number[i]:
            clues.append("Fermi")  # Sahi digit aur sahi jagah
        elif guess[i] in secret_number:
            clues.append("Pico")  # Sahi digit lekin galat jagah

    if not clues:
        return "Bagels"  # Koi sahi digit nahi hai
    else:
        clues.sort()
        return ' '.join(clues)

def is_valid_guess(guess):
    """Yeh function check karta hai ke guess valid 3-digit ka number hai ya nahi."""
    return len(guess) == 3 and guess.isdigit()

def play_bagels():
    print("Bagels mein khush amadeed!")
    print("Maine ek secret 3-digit number chhupa rakha hai. Usay guess karne ki koshish karo.")
    print("Hints: 'Pico' sahi digit lekin galat jagah ke liye, 'Fermi' sahi digit aur sahi jagah ke liye, aur 'Bagels' jab koi sahi digit nahi ho.")

    secret_number = get_secret_number()  # Ek random secret number generate karta hai
    attempts = 10  # 10 attempts milte hain

    for attempt in range(1, attempts + 1):
        guess = ""
        while not is_valid_guess(guess):
            guess = input(f"Guess #{attempt}: ")  # User se guess leta hai

        clues = get_clues(guess, secret_number)  # Clues return karta hai
        print(clues)

        if guess == secret_number:
            break  # Agar guess sahi ho to game end kar deta hai

    if guess != secret_number:
        print(f"Afsoos, aapke attempts khatam ho gaye. Secret number tha: {secret_number}.")

if __name__ == "__main__":
    play_bagels()  # Game ko start karta hai
