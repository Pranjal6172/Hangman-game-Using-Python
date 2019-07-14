# -*- coding: utf-8 -*-

import random

# for all the available letters after gussing each  letter
def availableletters(gussed_letter,wrong_gussed_letters):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    #combining both gussed letters and wrong gussed letters
    used_letters=gussed_letter+wrong_gussed_letters
    
    remaining_letters=""
    
    for i in alphabet:
        if(i not in used_letters):
            remaining_letters=remaining_letters+i+" "
    
    #returning remaining letters after each iteration 
    return remaining_letters
    
    
    
    
# for getting the correct word after each gussed letter 
def getGuessedWord(secretword,gussed_letters,blanks):
    
    count = len(gussed_letters)
    
    #when it matches to secret word
    if(''.join(blanks)==secretword):
       # print("test")
        return ''.join(blanks)
    #when no letter is gussed
    elif(count==0):
        #print("test1")
        return 'none'
    #for every iteration
    elif(gussed_letters[count-1] in secretword and ''.join(blanks)!=secretword):
        #selecting the indexes for matched chracter
        indexs=[i for i in range(len(secretword)) if secretword[i]==gussed_letters[count-1]]
        
        #filling blanks with matched character
        for i in indexs:
            blanks[i]=gussed_letters[count-1]
            
        #print(' '.join(blanks))
        #returning the final project
        return ' '.join(blanks)
    


def hangman(secretword):
    
    length_of_secretword=len(secretword)
    #correctly gussed letter
    gussed_letters=[]
    #wrong gused letter
    wrong_gussed_letters=[]
    # only 6 mistake are allowed
    mistake_allowed=6
    
    
    
    word_gussed=False
    
    #initially every thing is blank
    blanks = ['_ '] * len(secretword)
    
    print("secret word length is: "+str(length_of_secretword))
    print("Guess this word")
    
    while(mistake_allowed>0 and mistake_allowed<=6 and word_gussed==False):
        #if it is matched return that secret word
        if (secretword == str(getGuessedWord(secretword,gussed_letters,blanks))):
            word_gussed = True
            break
        
        print ("You have "+ str(mistake_allowed) + " guesses left.")
        print ("Available letters: " + availableletters(gussed_letters,wrong_gussed_letters))
        available_alpahbets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        #allowing machine to choose the word form 26 alphabets
        guess=random.choice(available_alpahbets)
        print("guessed letter: "+guess)
        
        if (guess in secretword):
            if(guess in gussed_letters):
                print("This letter is already gussed,choose another one")
                print("------------------------------")
                
            else:
                gussed_letters.append(guess)
                #filling the blanks after finding correct match
                print("Correct guess: " +str(getGuessedWord(secretword,gussed_letters,blanks)))
                
                
                print("------------------------------")
        else:
            if(guess in wrong_gussed_letters):
                print("This letter is already gussed,choose another one")
                print("------------------------------")
            
            else:
                wrong_gussed_letters.append(guess)
                mistake_allowed=mistake_allowed-1
                print("Wrong guess.")
                print("------------------------------")
                
            
    pridiction_divisor=len(gussed_letters)+len(wrong_gussed_letters)
    pridiction=(len(gussed_letters)/pridiction_divisor)*100
    
    if(word_gussed==True):
        print("****Congrats You Won the Game and your word is " +"'"+secretword+"'"+" ****")
        print("Prediction Accuracy: "+str(pridiction)+"%")    
        
        #return 'Congrats You Won The Game'
    elif(mistake_allowed==0):
        print()
        print("****Sorry, you ran out of guesses. The word was " +"'"+secretword+"'"+" ****")
        print("Prediction Accuracy: "+str(pridiction)+"%")
    


print("Welcome to Hangman")
print("-------------------------")
inputfile=open("words.txt",'rb',0)
wordslist=[]

for each_word in inputfile:
    wordslist.append(each_word.strip())
    
#print(wordslist)
#print(random.choice(wordslist))
#print(len(random.choice(wordslist)))

    
secretword=random.choice(wordslist).lower()
#print(secretword.decode("utf-8"))
hangman(secretword.decode("utf-8"))

