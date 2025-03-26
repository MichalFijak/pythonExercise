import random
import string

chars = " "+string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key=chars.copy()

random.shuffle(key)

text = input("Enter text to be encrypted!")
encrypted_text=""
for letter in text:
    encrypted_text+=key[chars.index(letter)]
print(f"Your orginal text : {text}")
print(f"Your encrypted text : {encrypted_text}")
decrypted=""
for letter in encrypted_text:
    decrypted+=chars[key.index(letter)]
print(f"Your decrypted text {decrypted}")