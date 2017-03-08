import bs4 as bs
import urllib.request
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import lxml
from sys import argv
from random_words import RandomWords
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from time import sleep

lemmatizer = WordNetLemmatizer()

def randomWord():
    #creates random word less than 6 characters in length
    while True:
        rw=RandomWords()
        randWord=rw.random_word()
        word=lemmatizer.lemmatize(randWord)
        if len(word) < 6:
            break
    return word

def sentencePrint(sentences):
    print("[DONE]")
    sleep(0.2)
    print("-------------------------------------")
    print("Here is your word used in a sentence!")
    print("-------------------------------------")
    print(*sentences, sep='\n')
    print("-------------------------------------")

def findWord():
    #tries out new words until a decent one is found
    while True:

        word = randomWord()

        #if url unfound, uses another word instead
        try:
            #collect url
            defsource = urllib.request.urlopen('http://www.dictionary.com/browse/'+word).read()
            
            #collect html from url
            defsoup = bs.BeautifulSoup(defsource,"html5lib")
            
            #used to check that there exists at least one sentence
            sentcount = 0

            #used to check that word is found within sentence
            wordPerSent = True

            #look for sentences that use the word
            sentarray = []
            for defdiv in defsoup.find_all('div', class_='def-block'):
                sentcount += 1
                wordFound = False
                wordarray = word_tokenize(defdiv.text)
                for i in range(len(wordarray)):
                    if ps.stem(wordarray[i].lower()) == ps.stem(word):
                        wordFound = True;
                        wordarray[i] = "______"
                sentence = " ".join(wordarray)
                sentarray.append(sentcount)
                sentarray.append(sentence)

                #if word not found in sentence
                if wordFound == False:
                    wordPerSent = False

            #proceeds if it finds at least 2 sentences, and the word appears at least once per sentence 
            if sentcount > 1 and wordPerSent == True:
                sentencePrint(sentarray)
                break
        except:
            pass

    return word

def Play():
    highscore = 0
    #until player doesn't want to play anymore
    while True:
        score = 0
        print("Your highscore: " + str(highscore))
        play = input('Start New Game? (y or n): ')
        if play.lower()=='y':
            
            #until the player loses their streak
            while True:

                print("Finding word... ", end="")
                
                #find word and sentences           
                word = findWord()
                    
                #request answer
                guess = input('Guess the word: ')

                print ('The word was ' + word)
                #check answer
                if lemmatizer.lemmatize(guess)==word:
                    score+=1

                    #update highscore
                    if highscore < score:
                        highscore = score;

                    print ("Your score is: " + str(score))
                else:
                    print("You Lose!")
                    break
        else:
            break


title = "Welcome To GUESS THE WORD!"
rules = "Each round, you will be given sentences and you have to guess what the missing word is. If you guess the word correctly, you will be awarded a point, and move on to the next round. If you fail to guess the word, you need to start all over."
for q in title:
    print(q, end="")
print("")
sleep(0.5)
print("########################")
sleep(0.5)

printTime = 0.005
while True:
    print("Rules are as follows:")
    for l in rules:
        print(l, end="")
        sleep(printTime)
    print("")
    sleep(0.5)
    print("-------------------------")
    sleep(0.5)
    ready = input("Are you ready to proceed to the game? (y or n): ")
    if (ready == "y"):
        break
    else:
        if printTime < 0.02:
            printTime += 0.02

Play()









