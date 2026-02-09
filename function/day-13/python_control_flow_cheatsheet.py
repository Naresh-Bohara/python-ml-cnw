"""
BEST INDUSTRY CONCEPTS CHEAT FILE
--------------------------------
Use this as a reference when coding.

RULE:
- Menus & fixed options  -> match-case
- Commands & dispatch   -> dictionary
- Tiny logic            -> if-else
"""

# =========================================================
# 1. MENUS & OPTIONS → match-case (BEST for CLI menus)
# =========================================================

def menu_example():
    print("\n--- MENU EXAMPLE (match-case) ---")
    print("1. Add")
    print("2. View")
    print("3. Exit")

    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Invalid input")
        return

    match choice:
        case 1:
            print("Adding...")
        case 2:
            print("Viewing...")
        case 3:
            print("Exiting menu")
        case _:
            print("Invalid option")

# WHY:
# - Fixed options
# - Clear flow
# - Most readable
# - Modern Python (3.10+)


# =========================================================
# 2. COMMANDS & DISPATCH → dictionary (BEST for extensible logic)
# =========================================================

def add():
    print("Add command executed")

def view():
    print("View command executed")

def delete():
    print("Delete command executed")

COMMANDS = {
    "add": add,
    "view": view,
    "delete": delete,
}

def command_example():
    print("\n--- COMMAND EXAMPLE (dictionary dispatch) ---")
    cmd = input("Enter command (add/view/delete): ").lower()

    action = COMMANDS.get(cmd)
    if action:
        action()
    else:
        print("Unknown command")

# WHY:
# - Easy to add new commands
# - No long if-elif
# - Used in CLIs, APIs, backends


# =========================================================
# 3. TINY LOGIC → if-else (BEST for small decisions)
# =========================================================

def tiny_logic_example():
    print("\n--- TINY LOGIC EXAMPLE (if-else) ---")
    age = int(input("Enter age: "))

    if age >= 18:
        print("Adult")
    else:
        print("Minor")

# WHY:
# - Only 2 conditions
# - Clean and obvious
# - No overengineering


# =========================================================
# MAIN DRIVER (just to test everything)
# =========================================================

if __name__ == "__main__":
    menu_example()
    command_example()
    tiny_logic_example()
