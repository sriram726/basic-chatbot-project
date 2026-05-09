# TASK 4: Basic Chat Program
# Conversation between You and Ram

def ram_chat():
    print("===================================")
    print("         YOU AND RAM CHAT")
    print("===================================")
    print("Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        # Greetings
        if user_input == "hello":
            print("Ram: Hi! Nice to meet you.")

        elif user_input == "good morning":
            print("Ram: Good morning! Have a great day.")

        elif user_input == "good night":
            print("Ram: Good night! Sweet dreams.")

        # Asking condition
        elif user_input == "how are you":
            print("Ram: I'm fine, thanks! How about you?")

        elif user_input == "i am fine":
            print("Ram: That's great to hear!")

        # Asking name
        elif user_input == "what is your name":
            print("Ram: My name is Ram.")

        # Asking age
        elif user_input == "how old are you":
            print("Ram: I am 20 years old.")

        # Asking place
        elif user_input == "where are you from":
            print("Ram: I am from India.")

        # Asking hobbies
        elif user_input == "what is your hobby":
            print("Ram: Playing games.")

        # Asking favorite color
        elif user_input == "what is your favorite color":
            print("Ram: My favorite color is blue.")

        # Asking favorite food
        elif user_input == "what is your favorite food":
            print("Ram: My favorite food is pizza.")

        # Asking study
        elif user_input == "what are you studying":
            print("Ram: I am studying computer science.")

        # Thank you message
        elif user_input == "thank you":
            print("Ram: You're welcome!")

        # Help command
        elif user_input == "help":
            print("Ram: You can ask simple questions or type bye to exit.")

        # Goodbye
        elif user_input == "bye":
            print("Ram: Goodbye! Have a nice day.")
            break

        # Unknown message
        else:
            print("Ram: Sorry, I don't understand that.")

# Function call
ram_chat()