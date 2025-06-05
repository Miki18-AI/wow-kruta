
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
new_alphabet = alphabet[::-1]
def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for latter in plaintext:
        if " " in latter:
            ciphertext += " " 
            continue
        index = alphabet.find(latter)
        new_index = (index + key) % 33
        new_latter = alphabet[new_index]
        ciphertext += new_latter
    return ciphertext
def tabs(plaintext):
    ciphertext1 = ""
    for latter in plaintext:
        if " " in latter:
            ciphertext1 += " "
            continue
        index = alphabet.find(latter)
        new_latter = new_alphabet[index]
        ciphertext1 += new_latter
    return ciphertext1


print(tabs('айтигенио'))
print(caesar_encrypt('кгтлфюегмхзфя рг тусдрсз кгрвхлз', -3))