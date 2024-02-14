# Intro to the app

print("""
*** WELCOME TO PERSONALIZED BIRTHDAY MESSAGE CREATOR!! ***
""")

# Collecting user information

print('''
Please enter recepient's name: ''')
recepient_name = input()

print('''
Please enter recepient's year of birth: ''')
recepient_year = int(input())

print('''
Please enter personalized message for the recepient: ''')
message = input()

print('''
Please enter sender's name: ''')
sender_name = input()


# Calculating the age of recepient

age = 2024 - recepient_year


# Creating the Birthday Message

print("")
print(recepient_name + ", let's celebrate your {} years of awesomeness!".format(age))

print("Wishing you a day filled with joy and laughter as you turn {}!".format(age))

print('''
''' + message + 
'''
''', 
'''
With love, and best wishes
''' + sender_name)