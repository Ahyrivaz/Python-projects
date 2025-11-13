#decrypt function
def rsa_decrypt(encrypted_message, d, n):
    return [pow(c, d, n) for c in encrypted_message]

d = 23           #Your parameter
n = 187          #Your parameter

encrypted_message = [30, 84, 48, 48, 155]    #encrypted message

decrypted_message = rsa_decrypt(encrypted_message, d, n)
print(f"Decrypted message: {decrypted_message}")
