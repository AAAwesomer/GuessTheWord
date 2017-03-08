# GuessTheWord
Simple word game that uses Net Scraping
8 hours of development.

Demonstrates basic use of NLP and algorithms.



What it does:

1. Introduces user to the game
2. Creates random word using the RandomWords library
3. Using Beautiful Soup 4, goes to the Dictionary.com url for that word and looks for sentences where the word is being used
4. If at least 2 sentences are found for that word, and the word shows up in each sentence at least once (accounts for word form), 
   proceeds to print the sentences into the Python Shell, with blanks for whenever the word shows up. Otherwise, repeats steps 2-4
5. Asks user to form a guess
6. If user guesses correctly, repeats steps 2-6, awarding the user a point for each correctly guessed word
7. Once the streak is over, overwrites the highscore if necessary, prints it to the console, and asks user to play again. If
   the response is affirmative, repeats steps 2-7, starting the score from 0.
8. If user decides to stop playing after a round, the game ends.
