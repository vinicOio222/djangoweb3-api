from string import ascii_letters, digits, punctuation
from random import choice

class Encryption:
    def generate_key(self, length: int = 32) -> str:
        chars = ascii_letters + digits + punctuation
        return ''.join([choice(chars) for _ in range(length)])
