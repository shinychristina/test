import time
name=input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
print ("")
time.sleep(1)
print ("Start guessing...")
time.sleep(0.5)
word= ("Secret")
word = word.lower()
guesses = ''
turns = 12
while turns > 0:
   failed = 0
   for char in word:
      guess = input("guess a character:")
      guesses += guess
      if char in guesses:
         print (char, )
      else:
         print ("_",)
         failed += 1
      if guess not in word:
         turns -= 1
         print ("Wrong")
         print("You have", + turns, 'more guesses' )
         if turns == 0:
            print("You Loose")
   if failed == 0:
      print ("You won" )
      break
      print
