def get_number_in_range(min_value, max_value):
  while True:
    try:
      user_input = input(f"Enter a number between {min_value} and {max_value}: ")
      number = int(user_input)
      if min_value <= number <= max_value:
        return number
      else:
        print(f"Please enter a number between {min_value} and {max_value}.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def pressAnyKeyToContinue():
    input("Press any key to continue...")

