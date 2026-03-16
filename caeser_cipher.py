#CAESAR CIPHER

password = input("Please create your password: ")
shift = input("Number of shifts: ")
while shift.isdigit() == False:
    shift = input("Number of shifts: ")
shift = int(shift)


encoded_password = ""
current_ord = 0
for i in range(len(password)): #Scrambles each character for encoded passsword

    if password[i].isdigit(): #Changes digits
        current_ord = ord(password[i])
        current_ord += shift
        while current_ord > 57:
            current_ord -= 10
        encoded_message += chr(current_ord)

    elif password[i].isalpha(): #Changes letters
        current_ord = ord(password[i])
        current_ord += shift
        if password[i].islower():
            while current_ord > 122:
                current_ord -= 26
        elif password[i].isupper():
            while current_ord > 90:
                current_ord -= 26
        encoded_message += chr(current_ord)

    else: #Leaves spaces and special characters the same
        encoded_message += password[i]


pass_attempt = ""
pass_correct = False
for attempt in range(5, 0, -1): #User inputs password to view their encoded password
    print(f"Attempts remaining: {attempt}")
    pass_attempt = input("Please enter your password: ")
    if pass_attempt == password:
        print(f"Encoded password: {encoded_message}")
        pass_correct = True
        break
    else:
        print("Incorrect.")

        
if pass_correct == False: #if user exhausts all 5 attempts their "account" is temporarily deactivated
    print("You are out of attempts. Please try again later.")
