
class WordleGame:
    maximum_attempts = 6
    value_of_change_string = "*"

    # constructor
    def __init__(self, wordle_word: str):
        self.secret: str = wordle_word.upper()
        self.attempts = []

    def attempt(self, word: str):
        self.attempts.append(word)

    def guess(self, word: str):
        word = word.upper()
        result = [CharacterCondition(x) for x in word]
        remaining_secret = list(self.secret)

        for i in range(5):
            letter = result[i]
            if letter.character == remaining_secret[i]:
                letter.word_present_and_at_place = True
                remaining_secret[i] = self.value_of_change_string

        for i in range(5):
            letter = result[i]

            if letter.word_present_and_at_place:
                continue

            for j in range(5):
                if letter.character == remaining_secret[j]:
                    remaining_secret[j] = self.value_of_change_string
                    letter.word_present = True
                    break
        return result

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.maximum_attempts - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
        pass


class CharacterCondition:
    def __init__(self, character: str):
        self.character: str = character
        self.character_size = 5
        self.word_present: bool = False
        self.word_present_and_at_place: bool = False

    def __repr__(self):
        return f"[{self.character} word_present: {self.word_present} word_present_and_at_place: {self.word_present_and_at_place}]"
