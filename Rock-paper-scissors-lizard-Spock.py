# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def number_to_name(number):
      if number ==0 :
        number = "rock"
      elif number == 1:
        number="Spock"
      elif number == 2:
        number="paper"
      elif number == 3:
        number="lizard"
      elif number == 4:
        number="scissors"   
      else:
        print "there is no such  name/number"
      return number

    
def name_to_number(name):
    if name == "rock":
        name = 0
    elif name == "Spock":
        name=1
    elif name == "paper":
        name=2
    elif name == "lizard":
        name=3
    elif name == "scissors":
        name=4   
    else:
        print "there is no such  name/number"
    return name


def rpsls(name): 
    player_number=name_to_number(name)
    comp_number=random.randrange(0,5)
    difference=(player_number-comp_number)%5
    if difference==1 or difference==2:
        output= "Player1 wins"
    elif difference==3 or difference==4:
        output= "Computer wins"
    elif difference==0:
        output= "Player and computer tie!"
    else:
        output ="something went wrong!!!!!!!!"
    name_comp= number_to_name(comp_number)
    print " "
    print "Player chooses", name
    print "Computer chooses", name_comp
    print output
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


