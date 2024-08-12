def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(texting, shifting):
  decipher_text = ""
  for letter in texting:
    deposition = alphabet.index(letter)
    new_deposition = deposition - shifting
    decipher_text += alphabet[new_deposition]
print(f"{decipher_text}")