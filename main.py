#Quiz Game
#Define the questions and answers

questions = ["What is the main male character name of the series of Vampire Diaries?","What is the name of the female character in the series of Vampire Diaries?", "The name of series which is sequel of vampire diaries?"]
answers = ["Damon", "Elena", "The Originals"]

#Initialize the score
score = 0

#Iterate through the questions
for i in range(len(questions)):
   #Display the question
   print(questions[i])
   #Get the user's answer
   user_answer = input("Your answer: ")
   #Check if the answer is correct
   if user_answer.lower() == answers[i].lower():
      print("Yeah! You got it right!!")
      score += 1
   else:
      print("Oopsieeee! That's not right!")
      print("The correct answer is:",answers[i])
     
print()  #Add a line break for readability
#Display the final score
print("Your final score is:", score)