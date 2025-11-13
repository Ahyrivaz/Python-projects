#Encrypt function
def rsa_encrypt(message, e, n):
    return [pow(m, e, n) for m in message]

e = 7      #Your parameter
n = 187    #Your parameter

message_blocks = [72, 101, 108, 108, 111,]  #The message is encoded using ASCII

encrypted_message = rsa_encrypt(message_blocks, e, n)
print(f"Encrypted message: {encrypted_message}")
