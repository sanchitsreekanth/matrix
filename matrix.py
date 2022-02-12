import time
import os
from termcolor import colored
lines = {
    "Transmission complete....": 0.03,
    "Wake up Parvathy ...": 0.3,
    "The Matrix has you.": 0.2,
    "Follow the white rabbit ...": 0.1,
    "Knock knock.": 0.1,
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()
for line, delay in lines.items():
    if line.startswith("Wake up"):
        time.sleep(4)
    else:
        time.sleep(2)

    for index, character in enumerate(line):
        print(colored(character, "green", attrs=["bold"]), end="", flush=True)
        if line.startswith("Wake up") and index in range(7, len(line) - 3):
            time.sleep(0.5)
        else:
            time.sleep(delay)
    if line.startswith("Transmission"):
        time.sleep(2.5)
    else:
        time.sleep(2)

    if not line.startswith("Knock"):
        os.system("clear")
time.sleep(3)
clear()
