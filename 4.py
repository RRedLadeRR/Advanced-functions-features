#Timofey
alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

def caesar_cipher(text, shift):
    encrypted_text = ''
    
    for char in text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            char_lower = char.lower()
            index = alphabet.index(char_lower)
            
            new_index = (index + shift) % len(alphabet)
            
            new_char = alphabet[new_index]
            encrypted_text += new_char.upper() if is_upper else new_char
        else:
            encrypted_text += char
    
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

input_text = input("Введіть текст: ")
shift = int(input("Введіть кількість букв на яке буде зроблений здвиг(ціле число): "))

encrypted_text = caesar_cipher(input_text, shift)
print(f"Зашифрований текст: {encrypted_text}")

decrypted_text = caesar_decipher(encrypted_text, shift)
print(f"Розшифрований текст: {decrypted_text}")