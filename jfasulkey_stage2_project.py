#blanks
blanks = ["___1___", "___2___", "___3___", "___4___"]

#questions by difficulty level
easy_questions = "There are " + blanks[0] +" days in a year, and " + blanks[1] + " days in a week. If you break down the weeks in a year, there are " + blanks[2] + " weeks in a year. Out of the 12 months in a year, " + blanks[3] + " months are 31 days long."
medium_questions = "The state of CA sits comfortably on the " + blanks[0] +" coast of USA. It's massive " + blanks[1] +" is the largest in the country, and is larger than several countries. A driving force of that has been the " + blanks[2] +" sector, positioned in northern CA. The city of " + blanks[3] +" has the largest population in the state."
hard_questions = "The biggest sports network on american tv is known as " + blanks[0] +" , and broadcasts primarily from studio facilities located in the state of " + blanks[1] +". It was founded in " + blanks[2] +" and has been able to stay relevent since then. The number one produced show on the network is known as " + blanks[3] +" and has been the flagship show since day one of the networks inception."

#difficulty levels
difficulty_levels = ["easy", "medium", "hard"]

#answers by answer level
easy_answers= [["365"],["7"],["52"],["7"]]
medium_answers = [["west"], ["economy"], ["tech", "technology"], ["la", "los angeles"]]
hard_answers= [["espn"], ["connecticut", "conn"], ["1979"], ["sportscenter", "sc"]]

def first_thing ():
	""" very first question, what game are they going to play. users selects difficulty_level then loads quiz_chosen.   """
	difficulty_chosen = raw_input("\nPlease select a game difficulty by typing it in! Possible choices include easy, medium, or hard:" )
	print ("\nYou choose " + difficulty_chosen + "!\n")
	while difficulty_chosen not in difficulty_levels:
		print difficulty_chosen + " is not a choice.\n"
		difficulty_chosen = raw_input("Please select a game difficulty by typing it in! Possible choices include easy, medium, or hard:" )
	if difficulty_chosen == "easy":
		return questions(easy_answers, easy_questions)
	elif difficulty_chosen == "medium":
		return questions(medium_answers, medium_questions)
	elif difficulty_chosen == "hard":
		return questions(hard_answers, hard_questions)

def questions(their_answer, quiz_question):
	""" this asks the questions and determines if the answers are correct or not. user can get the answer wronge 5 times before headed to the next function- win or lose. """
	i, chances = 0, 5
	while i < len(blanks) and chances > 0:
		print "\n" + quiz_question + "\n"
		user_answer = raw_input("What should be substituted for " + blanks[i] + ":" )
		user_answer = user_answer.strip( ' .' )
		user_answer = user_answer.lower()
		if user_answer in their_answer[i]:
			quiz_question = quiz_question.replace(blanks[i], user_answer)
			print "\nThat's Correct!"
			i += 1
		else:
			chances -= 1
			print "\n" + user_answer + " is not correct.\n\nYou have " + str(chances) + " chances left!\n"
	return win_or_lose(quiz_question, chances)				

def win_or_lose(quiz_question, chances):
	""" restarts the quiz based upon if they won or lost"""
	if chances != 0:
		print "\n" + quiz_question
		print "\nGreat work!!\n"
	elif chances ==0:
		print "\nSorry, you lost!\n"
	lets_go = raw_input("Would you like to play again? (y or n): ")
	if lets_go == "y":
		print first_thing()
	else:
		return "\nThanks for playing!"

print first_thing() #starts things off.
