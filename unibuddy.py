# This is UniBuddy chatbot. It will help freshman students with basic 
# information about university including events, clubs and FAQ. 

# A function to collect user age
def get_age():
    while True:
        try:
            user_age=int(input("Please enter your age?: "))
            return user_age
        except ValueError:
            print("Invalid entry. Please enter your age:")

# A function to request user favourite colour
def get_fav_colour():
     return input("Please enter your favourite colour: ").lower()

# A function to suggest clubs based on a colour choice
def colour_suggestions(fav_colour):
    if fav_colour == "red": 
        print("""
If red is your favorite color, I have the following for you:
1. Red themed Eagle Club
2. Red Dancing Club 
3. Our red themed music club
           """)
    
    elif fav_colour == "blue":
        print("""
If blue is your favorite color, I have the following for you:
1. Blue Ocean Club
2. Eagle Club
3. Swimming Shark Club
           """)

    elif fav_colour == "green":
        print("""
If green is your favorite color, I have the following for you:
1. Nature Lovers Club
2. Go Green Club 
3. Environmental Club
           """)
    elif fav_colour== "yellow":
        print("""
If yellow is your favorite color, I have the following for you:
1. Beach Club
2. Yellow themed Running Club 
3. Our yellow themed cinema club
           """)
    
    elif fav_colour == "black":
        print("""
If black is your favorite color, I have the following for you:
1. After midnight club
2. Our black themed karaoke club 
3. Black Martial Arts Club
           """)
    
    elif fav_colour == "pink":
        print("""
If pink is your favourite colour, I have the following for you:
1. Sugar Baking Squad
2. Women for women club
3. Pink themed university choir
""")
    else: 
       print("Oh no! I don't have any suggestions about this colour yet.")

# A unction to suggest events based on user age
def age_events(age):
    if age <=25:
        print("Freshman Party on 20/08 \nFoam Party on 28/08 \nNight of lasers on 29/08 \nDisco Night on 30/08 ")
    elif age >25 and age <= 35:
        print("\nNight of Colours on 19/08\n Painting and Dancing on 25/08\nSing out loud on 28/08\nMeditation Station Brunch on 29/08 ")
    elif age >35 and age <= 50:
        print("\nYoga Yoga lunch on 17/08\nKaraoke Night on 23/08\nCocktail Party on 25/08\nHiking on 29/08")
    else:
        print("\nDinner and candlelight on 19/08\nPicnic on 25/08\n80s Party and Dancing on 28/08 \nKaraoke on 1/09")

# A function that present FAQ and ask user to select specific question
def FAQ():
    while True:
        question=int(input("""
This is our FAQ
Please choose a number from the list and I will be happy to help (to quit type 0):

1. How do I find a library?
2. Where is the nearest bookstore located?
3. How can I join university clubs?
4. How can I become a part of university governance?
5. Where is the nearest public transport? 
6. Are there any scholarships available? """))

        if question == 1: 
            print("The library is on the left side of the entrance. You can find a map on the university website.")
        elif question == 2: 
            print(" The nearest bookstore is on London Road, a 5-minute walk from the university.")
        elif question == 3: 
            print("To join a club you need to contact the club representative. You can find the list of representatives on the university website.")
        elif question == 4:
            print("To become a part of university governance, you must submit your application to the main office.")
        elif question == 5:
            print("The nearest public transport is bus number 25, which will take you to the city centre.")
        elif question == 6:
            print("We offer a wide range of scholarships for our students. The list of scholarships will be available on 20/08.")
        elif question == 0:
            print("If you need more information, please check out our website www.imaginaryuniversity.co.uk")
            break
        else:
            print("Please select a number from 1 to 6")
        
# Main function to execute the program
def main():
    print("Hello! My name is UniBuddy and I am here to assist you.\nPlease enter your credentials so we can start. ")

    name = input("What is your name?: ")
    age = get_age()
    fav_colour = get_fav_colour()

    print(f"""
Hello {name.capitalize()}! It's a pleasure to meet you.
I can see that your favourite colour is {fav_colour}.
I have some suggestions for you.""")
    
    colour_suggestions(fav_colour)
    
    print(f"I can see that you are {age} years old. I have some age related events for you:")
    age_events(age)
    FAQ()

    print(f"It was nice chatting with you, {name.capitalize()}! Hope you will have a wonderful time studying at our university.")

if __name__ == "__main__":
    main()
    

    

        
            
    
    


















