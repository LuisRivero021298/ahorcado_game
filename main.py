import random

GAME_WORDS = ["Palabra", "Futbol", "Playstation", "Iphone", "Calculadora", "Ferrari", "Ronaldo"]

def getWordDict(word):
  word_dict = {}
  i = 0
  for item in word:
    word_dict[i] = { "letter": item.lower(), "match" : False }
    i += 1
  return word_dict

def run():
  #select word of list
  play_word = random.choice(GAME_WORDS)

  word_dict = getWordDict(play_word)
  
  letter_matches = 0
  while letter_matches < len(play_word):
    #show separated word
    space_print = ''
    for i in word_dict:
      if(word_dict[i]["match"] == False):
        space_print = space_print + '_ '
      else:
        space_print = space_print + word_dict[i]["letter"] + ' '
    print(space_print)

    #get user's letter
    user_letter = input('Inserte una letra: ')

    #if user's letter includes in the selected word, then show this letter
    y = 0
    for letter_play in play_word:
      if letter_play.lower() == user_letter.lower():
        word_dict[y]['match'] = True
        letter_matches += 1
      y += 1


  print('Felicitaciones has ganado')

if __name__ == '__main__':
  run()