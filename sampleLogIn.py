# Write your code here :-)

print('Type in correct username.')

userName = 'Alice'
for userNameGuessesTaken in range (1,4):

    name = input()      #Asks the user to type in their name.

    if name == '':
        print('Enter valid name. Username attempts = (' + str(int(userNameGuessesTaken)) + '/3).')

    elif name != userName:
        print('Try again.Username attempts = (' + str(int(userNameGuessesTaken)) + '/3).')
    else:
        break         #Breaks for expression. Continues to correct or incorrect username paths.
if name == userName:
    print ('Welcome. Please enter your password')

    for passwordGuessesTaken in range (1,4):

        password = input()          #
        if  password == '':
            print('Please type in a valid password. Password attempts = (' + str(int(passwordGuessesTaken)) + '/3).')
        elif password != 'swordfish':
            print('Incorrect password. Try again. Password attempts = (' + str(int(passwordGuessesTaken)) + '/3).')

        else:
            break
    if password == 'swordfish':
        print('Welcome, Alice')     #The user correctly inputted both the username and password.
    else:
        print('Password attemp failed 3 times. Account locked. Contact IT support.')        #Correct username but incorrect password after 3 attempts.
else:
    print('You are not a valid user. Account locked. Contact IT Support.') #Incorrect username. Locked out of account.


