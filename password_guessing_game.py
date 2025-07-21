import random

# 1. Define password lists by difficulty
easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "puzzle", "whale", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("---WELCOME TO THE PASSWORD GUESSING GAME---")
print("Choose the difficulty level: easy, medium or hard")

# 2. User chooses difficulty
level = input("Enter difficulty: ").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words) 
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice! Defaulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password!")

# 3. Game loop
while True:
    guess = input("Enter your Guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f'Congratulations! You guesssed it in {attempts} attempts.')
        break
    else:
        # 4. Give a hint: show which letters are correct
        hint = ""

        for i in range(len(secret)):
            if i < len(guess) and secret[i] == guess[i]:
                hint += guess[i]
            else:
                hint += "_"

        print("Hint: ", hint)