def translate(phrase):
    vowels = "aeiou"
    transation = ""
    for letter in phrase:
        if letter in vowels.upper():
            transation = transation + "M"
        elif letter in vowels:
            transation = transation + "m"
        else:
            transation = transation + letter
    return transation


print(translate(input("Enter a phrase: ")))
