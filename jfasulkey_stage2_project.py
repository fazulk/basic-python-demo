#blanks
blanks = ["___1___", "___2___", "___3___", "___4___"]

#questions by difficulty level
easy_questions = "There are " + blanks[0] +" days in a year, and " + blanks[1] + " days in a week. If you break down the weeks in a year, there are " + blanks[2] + " weeks in a year. Out of the 12 months in a year, " + blanks[3] + " months are 31 days long."
medium_questions = "The state of CA sits comfortably on the " + blanks[0] +" coast of USA. It's massive " + blanks[1] +" is the largest in the country, and is larger than several countries. A driving force of that has been the " + blanks[2] +" sector, positioned in northern CA. The city of " + blanks[3] +" has the largest population in the state."
hard_questions = "The biggest sports network on american tv is known as " + blanks[0] +" , and broadcasts primarily from studio facilities located in the state of " + blanks[1] +". It was founded in " + blanks[2] +" and has been able to stay relevent since then. The number one produced show on the network is known as " + blanks[3] +" and has been the flagship show since day one of the networks inception."

#answers by answer level
easy_answers= [["365"],["7"],["52"],["7"]]
medium_answers = [["west", "West"], ["economy", "Economy"], ["tech", "technology", "Technology"], ["la", "LA", "los angeles", "Los Angeles"]]
hard_answers= [["ESPN", "espn"], ["Connecticut", "connecticut", "conn", "Conn", "CONN"], ["1979"], ["sportscenter", "sc", "Sportscenter"]]

def first_thing ():# very first question, what game are they going to play. users selects difficulty_level then loads quiz_chosen.
	print
	difficulty_level = raw_input("Please select a game difficulty by typing it in! Possible choices include easy, medium, or hard:" )
	input = raw_input
	print
	print ("You choose " + difficulty_level + "!")
	return quiz_chosen(difficulty_level)

def quiz_chosen(quiz): #prints the quiz based upon the users input
	if quiz == "easy":
		print
		return questions(easy_answers, easy_questions)
	elif quiz == "medium":
		print
		return questions(medium_answers, medium_questions)
	elif quiz == "hard":
		print
		return questions(hard_answers, hard_questions)
	else:
		print
		print "Sorry " + quiz + "'s not an option."
		return first_thing()

def questions(their_answer, quiz_question): #asks the questions and determines if the answers are correct or not. user can get the answer wrong 5 times before having to restart the entire quiz over.
	i = 0
	chances = 5
	while i < 4:
		print quiz_question
		print
		user_answer = raw_input("What should be substituted for " + blanks[i] + ":" )
		if user_answer in their_answer[i]:
			print
			print "That's Correct!"
			print
			quiz_question = quiz_question.replace(blanks[i], user_answer)
			i += 1
		else:
			chances = chances - 1
			if chances < 1:
				print "Sorry, you lost!"
				return first_thing()
			else:
				print user_answer + " is not correct."
				print "You have " + str(chances) + " chances left!"
				print
	print quiz_question
	return play_again()


def play_again(): #asks to restart the quiz once they have passed to see if the user wants to play agian. or simply stop the program.
	print
	print "Great work!!"
	print
	lets_go = raw_input("Would you like to play again? (y or n): ")
	if lets_go == "y":
		print first_thing()
	else:
		print
		return "Thanks for playing!"

print first_thing() #starts things off.
