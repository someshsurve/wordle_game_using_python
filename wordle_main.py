import os
import random
from wordle_logic import WordleGame
from colorama import Fore


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


def main():
    word_set = load_word_set("words_source_coditation.txt")
    random_select = random.choice(list(word_set))
    wordle = WordleGame(random_select)

    while wordle.can_attempt:
        x = input("Please, guess your word : ").upper()

        if len(x) != 5:
            print(Fore.RED + f"Word must be 5 characters long" + Fore.RESET)
            continue

        if x not in word_set:
            # os.system('cls')
            print(Fore.RED + f"{x}"+Fore.RESET+" seems Invalid word!")
            continue

        wordle.attempt(x)
        result = wordle.guess(x)
        wordle_show(wordle)

    if wordle.is_solved:
        print("******** You've solved the puzzle ********")
    else:
        print("        You Lost!!!")
        print(f"the word was: {wordle.secret}")


def wordle_show(wordle: WordleGame):
    lines = []
    for word in wordle.attempts:
        result = wordle.guess(word)
        result2 = []
        for letter in result:
            if letter.word_present_and_at_place:
                color = Fore.GREEN
            elif letter.word_present:
                color = Fore.YELLOW
            else:
                color = Fore.WHITE

            colored_letter = color + letter.character + Fore.RESET
            result2.append(colored_letter)
        lines.append("  ".join(result2))

    for i in range(wordle.remaining_attempts):
        lines.append(" ".join(["--"] * 5))

    for x in lines:
        print(x)
    print(f"{Fore.RED}\nWarning: {Fore.RESET}{Fore.BLUE}{wordle.remaining_attempts}{Fore.RESET} attempts remaining\n")


if __name__ == "__main__":
    main()
