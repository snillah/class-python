import os
import json
import datetime

# File to store journal entries
FILENAME = "journal.json"

def load_entries():
    """Load existing journal entries"""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []   # Return empty list if file doesn't exist

def save_entries(entries):
    """Save entries to JSON file"""
    try:
        with open(FILENAME, "w") as file:
            json.dump(entries, file, indent=4)
    except FileExistsError:
        print("No file Exist")

def add_entry():
    """Add a new journal entry"""
    text = input("Write your journal entry: ")
    entry = {
        "date": str(datetime.datetime.now()),
        "content": text
    }
    entries = load_entries()
    entries.append(entry)
    save_entries(entries)
    print("✅ Entry saved successfully!\n")

def view_entries():
    """Display all journal entries"""
    entries = load_entries()
    if not entries:
        print("No entries found yet.\n")
        return
    for e in entries:
        print(f"📅 {e['date']}")
        print(f"📝 {e['content']}")
        print("-" * 40)

def main():
    """Main menu"""
    while True:
        print("\n=== Daily Journal App ===")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ")
        
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Thanks =>Goodbye ")
            break
        else:
            print("Invalid choice! Try again.\n")

main()
