def encoder(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            shifted = chr((ord(char) - ord('a') + 15) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') + 15) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(char)
    return "".join(result)

text = input("Enter text: ")

print("Encoded text is: ",encoder(text))
