import os
from dotenv import load_dotenv

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_pretty_link():
    load_dotenv()  # ✅ Load from .env
    link = os.getenv("GANDALF_LINK")

    clear_screen()
    print("\n" * 5)
    print("=" * 60)
    print("\n" + "🔗 Visit the challenge link below:".center(60))
    print("\n" + link.center(60) + "\n")
    print("=" * 60)
    print("\n" * 5)

