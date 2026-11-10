messages_history = []

def save_messages(role, message):
    messages_history.append({"role" : role, "message" : message})

def show_history():
    print("--------------HISTORY--------------")
    for item in messages_history:
        print(f"{item['role']}: {item['message']}")
    print("-----------------------------------")

def start_conversation():
    print("\n Hello my dear friend. How you feel? :)")
    print("\n type exit when you want our chat to end.")
    while True:
        user_message = input("You : ")

        if user_message.lower() == "exit":
            print("okay...good bye and stay safe :)")
            break

        if user_message.lower() == "history":
            show_history()
            continue

        save_messages("User", user_message)
        lily_respond = "HOLDER - received: " + user_message
        save_messages("Lily", lily_respond)

        print("Lily: " + lily_respond)

def main():
    print("Lily is booting up and getting ready.")
    start_conversation()

if __name__ == "__main__":
    main()
