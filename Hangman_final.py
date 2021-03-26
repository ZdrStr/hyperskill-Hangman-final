import random
import string
#https://www.geeksforgeeks.org/python-multiple-indices-replace-in-string/
print("H A N G M A N")
list_names = ['kotlin', 'javascript']#['python', 'java']
word_1 = random.choice(list_names)
word_2 = "-" * (len(word_1))
temp_list = list(word_2) # This line can be removed and simply add list(word_2)
guessed = set()
count = 8
while True:
  game=input('Type "play" to play the game, "exit" to quit:')
  if game == "play":
    while count > 0:
      letter = input(f"\n{str(word_2)}\nInput a letter:")
      index_1 = [str(i) for i, e in enumerate(word_1) if e == letter]
  
      for index_num in index_1:
        temp_list[int(index_num)] = letter
        word_2 = "".join(temp_list)
  
      if word_1 == word_2:
        print("\n")
        print(word_1)
        print("You guessed the word!\nYou survived!")
        break
      elif len(letter) != 1:
        print("You should input a single letter")
  
      elif letter not in string.ascii_lowercase:
        print("Please enter a lowercase English letter")
  
      elif letter in guessed and letter not in list(word_1):
        print("You've already guessed this letter")
    
      elif letter in guessed:
        print("You've already guessed this letter")
  
      elif letter not in list(word_1):
        count -= 1
        print("That letter doesn't appear in the word")

      guessed.add(letter)  
    else:
      print("You lost!")
      print()# types of new line ( """",''',\n, print())
  elif game == "exit":
    break
