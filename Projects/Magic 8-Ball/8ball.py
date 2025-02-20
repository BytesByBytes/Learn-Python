import random

#Variables for the 8 ball
name = "Joe"
question = "Will I be rich this year? "
answer = ""


#User Inoput 
 





random_number = random.randint(1,9) #storing the random number 


#if statements for the 8 ball answers 
if random_number == 1:
  answer = "Yes - Definatly"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "Better not tell you now"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very dountful"
else:
  answer = "Error"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " +answer)