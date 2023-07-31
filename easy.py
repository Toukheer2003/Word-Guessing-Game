from easy_words import *
import random

word=random.choice(words)
print('Guess the correct alphabets(type in lower case only)','\nYou have 12 turns','\nFor every correct guess you retain your turn','\nFor every wrong guess..you lose that turn','\nYou can start by choosing a random alphabet')
print('Good luck')
print('All the best!!')

guesses=''
turns=12
s=random.sample(word,3)
i=0
for i in range(0,3):
	global gf
	global gh
	global gk
	gf=s[0]
	gh=s[1]
	gk=s[2]
		
while turns>0:
	failed=0
	for char in word:
		if char in gf:
			print(gf)
		elif char in gh:
			print(gh)
		elif char in gk:
			print(gk)
		elif char in guesses:
			print(char)
		else:
			print('_')
			failed+=1
	if failed==0:
		print("You win")
		print('Congratulations!!')
		break
	guess=input('Guess a character:')
	guesses+=guess
	if guess not in word:
		turns-=1
		print('Wrong')
		print('You have',turns,'more guesses')
		if turns==0:
			print('Tough luck','\nBetter luck next time')
		elif turns==11:
			print('Try again')
		elif turns==5:
			print('Try harder')
		elif turns==8:
			print('You can do it')
		elif turns==1:
			print('Your turns are ending..') 
	if guess in word:
		
		if guess==gf:
			print('Try another word')			
		elif guess==gh:
			print('Try another word')
		elif guess==gk:
			print('Try another word')
		elif turns==12:
			print('You have started well..')
		elif turns==7:
			print('Keep it up')
		elif turns==4:
			print('A few more of those good guesses and you win')
		elif turns==1:
			print("That's close..")

print('The word is:',word)
i=input('Thank You')
