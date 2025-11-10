HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:   #open the file
            lines = file.readlines()  #reads all lines in the file and puts them in a list.
    except FileNotFoundError:
        lines = []

    if len(lines) == 0:
        print("No history found")
    else:
        for l in reversed(lines):
            print(l.strip())


def clear_history():
    # opening in 'w' mode clears the file
    with open(HISTORY_FILE, 'w'):
        pass
    print('History Cleared')


def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{equation} = {result}\n")


def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use format: number operator number (e.g. 5 + 2)")
        return

    # Validate numeric conversion
    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers. Make sure you entered valid numbers (e.g. 3.5  +  2).")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*" or op.lower() == "x":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use one of: +  -  *  /")
        return

    # make integer-looking floats print as ints
    if isinstance(result, float) and result.is_integer():
        result = int(result)

    print("Result:", result)
    save_to_history(user_input, result)


def main():
    print("--- SIMPLE CALCULATOR (type: history, clear, or exit) ---")
    while True:
        user_input = input("Enter calculation (e.g. 5 + 2) or command (history, clear, exit): ").strip()
        if user_input.lower() == "exit":
            print("Goodbye")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculate(user_input)


if __name__ == "__main__":
    main()
