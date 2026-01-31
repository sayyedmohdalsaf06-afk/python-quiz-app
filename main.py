from quiz_engine import start_quiz

username = input("Enter your name: ")
print(f"\nAll the best, {username}!")

def welcome_screen():
    print("=" * 40)
    print("WELCOME TO THE SMART QUIZ APP")
    print("=" * 40)
    print("Rules:")
    print("1. Each question has 4 options")
    print("2. Enter option number (1-4)")
    print("3. Each correct answer gives 1 point")
    print("=" * 40)

def show_result(score, total):
    percentage = (score / total) * 100

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 50:
        print("Good job! Keep practicing.")
    else:
        print("Needs improvement. Try again!")

if __name__ == "__main__":
    welcome_screen()
    input("Press Enter to start the quiz...")
    score, total = start_quiz()
    show_result(score, total)
