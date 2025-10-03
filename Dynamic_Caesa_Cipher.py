alphabet = "abcdefghijklmnopqrstuvwxyz"

answer = input("Enter text to encrypt: ").lower()
N = int(input("Enter your number in the journal: "))

key = ((N**2) + 7) % 13  #or any formula
code = ''

for el in answer:
    if el == ' ':
        code += ' '
    elif el in alphabet:
        new_id = alphabet.index(el) - key
        code += alphabet[new_id % len(alphabet)]
    else:
        code += el

print("Shifted to the left by", key, "positions")
print(code)
