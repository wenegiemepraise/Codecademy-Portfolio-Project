import time
import threading
#Who wants to be a millionaire
print("Welcome to who wants to become a millionaire featuring your host 'Praise Wenegieme' ")
#First get challanger information
class Contestant():
    def __init__(self):
        self.name = input("\nWhat is your name: ").title()

        while True:
            age = input("\nHow old are you? ")
            if age.isdigit():
                self.age = int(age)
                break
            else:
                print("\nPlease enter a valid name!")

        self.occupation = input("\nWhat is your occupation? ").title()
        
        while True:
            amount_of_time = input("\nDo you want 15, 25 or 35 seconds to answer each question? ")
            if amount_of_time.isdigit():
                if int(amount_of_time) in [15, 25, 35]:
                    self.amount_of_time = int(amount_of_time)
                    break
            else:
                print("\nPlease pick a valid time")

        self.score = 0

    def __repr__(self) -> str:
        return f"This contestants name is {self.name}. They are {self.age} years old and their occupation is {self.occupation}" 
    
class Game():
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"This is the game class where we will host all our games!"

    def play(self, Contestant):
        print(f"\nCan have a round of applause for our contestant {Contestant.name} who will now be begins the game!!")

        while True:
            choice_quiz = input("\nWhat quiz do you want? General Knowledge, Sport, Computer Science: ")
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
                print("\nPlease choose a valid quiz!")

    def start_game(self):
        t = 10
        print("\nThe contest will start in 10 seconds!")    
        while t: 
            mins, secs = divmod(t, 60) 
            timer = f'{mins:02d}:{secs:02d}'
            print(timer, end="\r") 
            time.sleep(1) 
            t -= 1
        
        return 'Lets the games begin!!'

    def timer_for_questions(self, Contestant, question_time, event):
        time_remaining = question_time

        while time_remaining > 0 and not event.is_set():
            minutes, seconds = divmod(time_remaining, 60)
            timer_for_q = f"{minutes:02d}:{seconds:02d}"
            print(timer_for_q, end="\r")
            time.sleep(1)
            time_remaining -= 1

        print()

        if not event.is_set():
            print("Times up!")
            event.set()
            

    def general_knowledge_quiz(self, Contestant):
        print(f"\nIt seems like we have an all rounder here folks. Lets test {Contestant.name} general knowledge.")
        self.start_game()

    def sport_quiz(self, Contestant):
        print(f"\nIt seems we have a sports fan here. Lets find out how much {Contestant.name} knows about sports!")
        self.start_game()

    def computer_science_quiz(self, Contestant):
        print(f"\nOoo it looks like we have a tech genius in our midst. Lets test {Contestant.name} knowledge on computer science!")
        self.start_game()

        print("Phase 1: Programming Languages")
        asked_computer_science_questions = []
        computer_science_questions = {"What is the most common programming language used in competitive programming?": "c++",
                                      "Name a COMPILED language.": ["c", "c++", "c#", "java", "rust", "go", "golang", "fortran", "swift"],
                                      "What does the acorynm SQL stand for?": "standard query language",
                                      "Which programming language was developed by Apple for building iOS and macOS applications?": "swift",
                                      "Name a DYNAMICALLY typed language.": ["lua", "python", "javascript", "php", "ruby", "perl", "r", "groovy", "shell scripting languages"]}
        
        for q, a in computer_science_questions.items():
            if q not in asked_computer_science_questions:

                timer_event = threading.Event()

                timer_thread = threading.Thread(target=self.timer_for_questions, args=(Contestant, Contestant.amount_of_time, timer_event))
                timer_thread.start()
                
                
                print(f"\r", end="")
                print(q)

                computer_science_answer = input("What is the answer: ")

                timer_event.set()
                timer_thread.join()

                if computer_science_answer.lower() == a or computer_science_answer.lower() in a:
                    print("You are correct")
                    Contestant.score += 1
                else:
                    print("Incorrect!")
                        

            asked_computer_science_questions.append(q)
        
        






game = Game()
praise = Contestant()
game.play(praise)



#Based on age set a specific questions
#Asked them if they want a certain category but if they get to pick their category they lose 50% of the prize
#Use time input import to track how long it takes to answer each question.
#Pick challangers randomly in order for the questions
#Allow each challanger 2 hints
#Challanger coule be a potential object
#They have to answer 10 or 15 questions and they can only get 2 or 3 wrong before they are disqualified
#Give out extra additional prizes for speed completion
