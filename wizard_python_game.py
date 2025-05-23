import random

def ask_question(a, b, op):
    """Calculate the correct answer based on the operation."""
    if op == '/' and b == 0:
        b = 1  # Prevent division by zero

    # Calculate the result
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return round(a / b, 2)  # Rounded to two decimals
    elif op == '**':
        return a ** b

def play_game():
    """Play a single round of 5 math questions."""
    operations = ['+', '-', '*', '/', '**']
    score = 0

    for _ in range(5):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(operations)
        result = ask_question(a, b, op)

        # Ask the player
        answer = input(f"What is {a} {op} {b}? ")

        # Try to check the answer
        try:
            if op == '/':
                if round(float(answer), 2) == result:
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ Incorrect. The correct answer was {result}")
            else:
                if int(answer) == result:
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ Incorrect. The correct answer was {result}")
        except ValueError:
            print("⚠️ That wasn't a number. No points this round.")

    print(f"\n🎯 Final Score: {score} out of 5\n")

def main():
    """Main loop for the game, allows replay."""
    print("🔢 Welcome to the Math Wizard Game!")
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("👋 Thanks for playing! Goodbye.")
            break

# Run the game
if __name__ == "__main__":
    main()