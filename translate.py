def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #estamos comprobando si letter esta dentro de este string, si esta dentro podemos saber que utiliza una vocal y modificarlo
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
           translation += letter
    return translation

print(translate(input("Enter your phrase: ")))
