import random
import os

GAME_WORDS = [
  { 
    "word": "Palabra",
    "clue": "Es lo que buscas"
  }, 
  { 
    "word": "Futbol",
    "clue": "Es una pasión"
  }, 
  { 
    "word": "Playstation",
    "clue": "Pirlo dijo que era el mejor invento del hombre"
  }, 
  { 
    "word": "Iphone",
    "clue": "3 elementos revolucionarios en uno solo - SJ"
  }, 
  { 
    "word": "Calculadora",
    "clue": "Un regalo especial para cualquier ingeniero"
  }, 
  { 
    "word": "Ferrari",
    "clue": "Caballo, Amarillo, nada más que agregar"
  }, 
  { 
    "word": "Ronaldo",
    "clue": "El mejor deportista de todos los tiempos"
  }
]

def getWordDict(word):
  word_dict = {}
  i = 0
  for item in word:
    word_dict[i] = { "letter": item.lower(), "match" : False }
    i += 1
  return word_dict

def clearConsole():
  if os:
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def getPlayWord():
  menu_statement = """ 
    Elige una de las siguientes opciones:
      Individual (1)
      Multijugador (2)
      Salir (3)
  """
  play_word = ""
  play_clue = ""

  while play_word == "":
    clearConsole()
    
    menu_options = input(menu_statement)
    if menu_options == "1":
      #select word of list
      random_word = random.choice(GAME_WORDS)
      play_word = random_word["word"]
      play_clue = random_word["clue"]
    elif menu_options == "2":
      play_word = input("Escribe una palabra: ").strip()
      play_clue = input("Escribe una pista: ").strip()
    elif menu_options == "3":
      print("Hasta luego ")
      exit()
    else:
      input("Debe elegir una opción correcta ")

  return { "play_word": play_word, "play_clue": play_clue }

def run():
  play_options = getPlayWord()
  play_word = play_options["play_word"]
  play_clue = play_options["play_clue"]

  if play_word != "":
    word_dict = getWordDict(play_word)
    
    letter_matches = 0
    while letter_matches < len(play_word):
      clearConsole()
      print(play_clue)
      #show separated word
      space_print = ''
      for i in word_dict:
        if(word_dict[i]["match"] == False):
          space_print = space_print + '_ '
        else:
          space_print = space_print + word_dict[i]["letter"] + " "
      print(space_print)

      #get user's letter
      user_letter = input("Inserte una letra: ")

      #if user's letter includes in the selected word, then show this letter
      y = 0
      for letter_play in play_word:
        if letter_play.lower() == user_letter.lower():
          word_dict[y]["match"] = True
          letter_matches += 1
        y += 1


    print("Felicitaciones has ganado")

if __name__ == '__main__':
  run()