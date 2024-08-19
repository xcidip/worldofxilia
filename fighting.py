import random
import time
from random import randint

import utility


def number_game(time_for_answer: int = 8):
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    answer = num1 + num2

    start_time = time.time()

    while True:
        guess = int(input(f"What is {num1} + {num2}? "))

        end_time = time.time()
        elapsed_time = end_time - start_time

        if guess == answer and elapsed_time < time_for_answer:
          print(f"Correct! Time taken: {elapsed_time:.2f} seconds")
          return True
        elif guess == answer:
            print(f"Correct! but too late :(")
            return False


def start_fight(fighting_style: str, player, enemy):
    if fighting_style == "number_game":
        while True:
            if hit(player, enemy):
                print("Enemy has won")
                break
            else:
                print("Player has won")
                break
    utility.press_any_key_to_continue()

def hit(player, enemy):
    # 70 percent roll
    if randint(1, 10) > 3:
        if enemy.take_damage(randint(player.min_damage, player.max_damage)):
            print(f"You beat {enemy.name}")
            return True
    else:
        print("Oops you missed.")
    if player.take_damage(randint(player.min_damage, player.max_damage)):
        print("You died, RIP!")
        return False