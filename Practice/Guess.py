secret_word = "giraffe" #palabra secreta
guess = "" #variable de adivinanza
guess_count = 0 #hacemo el conteo
guess_limit = 3 # limites de aciertos
out_of_guesses = False

while guess != secret_word and not(out_of_guesses): #si guees es diferente a palabra secreta,hacer instrucion a continuacion
    if guess_count < guess_limit: # si guess_count es menor a guess_limit hacer la intruccion
        guess = input("Enter guess: ") #haca ingresa la palabra
        guess_count += 1 # suma guess_count
    else:
        out_of_guesses = True #si no adivina
if out_of_guesses:
    print("Out of Guesses, You LOSE!") # si lo guess es
else:
    print("YOU WIN!") # si adivina
