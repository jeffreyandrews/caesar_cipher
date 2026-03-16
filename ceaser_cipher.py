#CEASER CIPHER

password = input("Please create your password: ")
shift = input("Number of shifts: ")
while shift.isdigit() == False:
    shift = input("Number of shifts: ")
shift = int(shift)

encoded_message = ""
current_ord = 0
for i in range(len(password)):
    if password[i].isdigit():
        current_ord = ord(password[i])
        current_ord += shift
        while current_ord > 57:
            current_ord -= 10
        encoded_message += chr(current_ord)
    elif password[i].isalpha():
        current_ord = ord(password[i])
        current_ord += shift
        if password[i].islower():
            while current_ord > 122:
                current_ord -= 26
        elif password[i].isupper():
            while current_ord > 90:
                current_ord -= 26
        encoded_message += chr(current_ord)
    else:
        encoded_message += password[i]

pass_attempt = ""
pass_correct = False
for attempt in range(5, 0, -1):
    print(f"Attempts remaining: {attempt}")
    pass_attempt = input("Please enter your password: ")
    if pass_attempt == password:
        print(f"Encoded message: {encoded_message}")
        pass_correct = True
        break
    else:
        print("Incorect.")
        
if pass_correct == False:
    print("You are out of attempts. Please try again later.")
