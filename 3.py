#Timofey
def count_characters(sentence):
    char_count = {}
    
    for char in sentence:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char, count in char_count.items():
        print(f"'{char}' = {count}")

sentence = input("Введіть речення: ")
count_characters(sentence)