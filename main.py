#Who wants to be a millionaire
print("Welcome to who wants to become a millionaire featuring your host 'Praise Wenegieme' ")
print("In todays episode we will take on two challangers and let them compete against eachother for the grand prize of 1 million euro!!")
#First get challanger information
class Contestant():
    def __init__(self):
        self.name = input("What is your name")

        while True:
            age = input("How old are you?")
            if age.isdigit():
                self.age = int(age)
                break
            else:
                print("Please enter a valid name!")

        self.occupation = input("What is your occupation? ")
        
        while True:
            amount_of_time = input("Do you want 15, 25 or 35 seconds to answer each question? ")
            if amount_of_time.isdigit():
                if amount_of_time in [15, 25, 35]:
                    self.amount_of_time = amount_of_time
                    break
            else:
                print("Please pick a valid time")

        self.score = 0

    def __repr__(self) -> str:
        return f"This contestants name is {self.name}. They are {self.age} years old and their occupation is {self.occupation}" 
    
class Game():
    def __init__(self) -> None:
        pass

    def play(self, Contestant):
        print(f"Can have a round of applause for our contestant {Contestant.name} who will now be begins the game!!")

        while True:
            choice_quiz = input("What quiz do you want? General Knowledge, Sport, Computer Science: ")
            if choice_quiz.lower() == "computer science":
                self.computer_science_quiz(Contestant)
                break

            elif choice_quiz.lower() == "general knowledge":
                self.general_knowledge_quiz(Contestant)
                break

            elif choice_quiz.lower() == "sport":
                self.sport_quiz(Contestant)
                break
            else:
                print("Please choose a valid quiz!")
            

    def general_knowledge_quiz(self, Contestant):
        print(f"It seems like we have an all rounder here folks. Lets test {Contestant.name} general knowledge.")

    def sport_quiz(self, Contestant):
        print(f"It seems we have a sports fan here. Lets find out how much {Contestant.name} knows about sports!")

    def computer_science_quiz(self, Contestant):
        print(f"Ooo it looks like we have a tech genius in the amoung. Lets test {Contestant.name} knowledge on computer science!")

#Based on age set a specific questions
#Asked them if they want a certain category but if they get to pick their category they lose 50% of the prize
#Use time input import to track how long it takes to answer each question.
#Pick challangers randomly in order for the questions
#Allow each challanger 2 hints
#Challanger coule be a potential object
#They have to answer 10 or 15 questions and they can only get 2 or 3 wrong before they are disqualified
#Give out extra additional prizes for speed completion
