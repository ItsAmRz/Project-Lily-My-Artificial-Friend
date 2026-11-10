def start_conversation():
    print("\n Hello my dear friend. How you feel? :)")
    print("\n type exit when you want our chat to end.")
    while True:
        user_message = input("You : ")

        if user_message.lower() == "exit":
            print("okay...good bye and stay safe :)")
            break

def main():
    print("Lily is booting up and getting ready.")
    start_conversation()

if __name__ == "__main__":
    main()
