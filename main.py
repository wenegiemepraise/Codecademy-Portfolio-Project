#Who wants to be a millionaire
print("Welcome to who wants to become a millionaire featuring your host 'Praise Wenegieme' ")
print("In todays episode we will take on two challangers and let them compete against eachother for the grand prize of 1 million euro!!")
#First get challanger information
def get_player():
    player_name = input("What is your name: ")
    print(f"Well {player_name} it is nice to have you today")

    while True:
        try:
            player_age = int(input("How old are you? "))
            if player_age < 0:
                print("Enough with the jokes 🤣. Please enter a valid age")
                continue
            if player_age < 30:
                print(f"Well folks we have a young challanger today at the bright age of {player_age}")
            elif player_age < 50:
                print(f"We seem to have a middle age contest today and the stellar age of {player_age}")

        except TypeError:
            print("Please enter a number!")
#Based on age set a specific questions
#Asked them if they want a certain category but if they get to pick their category they lose 50% of the prize
#Use time input import to track how long it takes to answer each question.
#Pick challangers randomly in order for the questions
#Allow each challanger 2 hints
#Challanger coule be a potential object
#They have to answer 10 or 15 questions and they can only get 2 or 3 wrong before they are disqualified
#Give out extra additional prizes for speed completion
