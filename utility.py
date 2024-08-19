def ask_and_get_number_in_range(text, min_value, max_value):
  while True:
    try:
      print(text)
      user_input = input(f"Enter a number between {min_value} and {max_value}: ")
      number = int(user_input)
      if min_value <= number <= max_value:
        return number
    except ValueError:
      print("Invalid input. Please enter a number.")

def press_any_key_to_continue():
    input("Press any key to continue...")

