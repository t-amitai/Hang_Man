import json
import time
import random as rand

def getJson():
	with open('hang_man.json', 'r') as read_file:
		data = json.load(read_file)
		read_file.close()
	return data


def display(image, errors=0):
	data = getJson()
	if image == "board":
		for row in data[image][errors]:
			print(row)
	else:
		for row in data[image]:
			print(row)
			
			
def get_word():
	with open('hang_man.json', 'r') as read_file:
		data = json.load(read_file)
		read_file.close()
	ls = []
	for w in data["words"]:
		ls.append(w)
	grab = data["words"][rand.randint(0, len(ls)-1)]
	word = []
	for i in grab:
		word.append(i)
	return word
	
	
def get_guess(score):
	for i in score:
		print(i, end = '')
	print('\n')
	inputting = True
	while inputting:
		letter = input('Which letter would you like to guess?\n').strip()
		if len(letter) != 1:
			print("invalid entry")
		elif letter.isalpha():
			inputting = False
		else:
			print("invalid entry")
	return letter.lower()
	
	
def check_guess(letter, word, score, errors):
	count = 0
	for i, let in enumerate(word):
		if let == letter:
			word[i] = '*'
			score[i] = let
			count += 1
	if count == 0:
		errors += 1
		print("Wrong guess! You have {} more tries.".format(10-errors))
	return word, score, errors
	

def check_score(score, errors):
	if errors >= 10:
		return False, False
	count = 0
	for let in score:
		if not let.isalpha():
			count += 1
	if count != 0:
		return True, False
	else:
		return False, True
	
	
def main():
	display("title")
	time.sleep(1)
	display("intro")
	input()
	word = get_word()
	saved_word = [None] * len(word)
	for i,letter in enumerate(word):
		saved_word[i] = letter
	score = ['*'] * len(word)
	errors = 0
	display("board")
	playing = True
	won = False
	while playing:
		letter = get_guess(score)
		word, score, errors = check_guess(letter, word, score, errors)
		display("board", errors)
		playing, won = check_score(score, errors)
	if won:
		for i in score:
			print(i, end='')
		print('\n')
		print("You won!")
	else:
		for i in saved_word:
			print(i, end='')
		print('\n')
		print("You've been hanged.")

		
if __name__ == "__main__":
	main()
	print("Game exiting.")
	time.sleep(5)
