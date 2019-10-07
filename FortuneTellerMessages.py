import random


# This is the list of random responses that will be given by the fortune teller
Answers = ['It is your future!',

'It is undoubtable', 'Obviously!!!', 'Yes, without a doubt',

'You can bet anything on it', 'For now it is a YES', 'Most likely',

'Your future looks bright', 'Signs point to a yes', 'I am not so sure', 'Try Again',

'Ask again later', 'Maybe you should not know', 'I cant give you a prediction right now',

'You should concentrate and ask again', 'Dont count on it that much', 'I think not', 'My sources say no',

'The future looks bad', 'Very doubtful', 'Sorry, but NO', 'Definite No']


#The Fortune Teller Introduces herself
print('Hello There, My name is Solstice, What is your name?')

#Fortune Teller ask for the user's name
Name = input("Please Enter Your Name Here So I can Start See Into Your Future Better: ")
print('Hello ' + Name)


def Solstice():
    #Solstice will ask for User's random question
    print('Ask me any question that you want answered.')
    input()

    print (Answers[random.randint(0, len(Answers)-1)] )
    print('I hope that I have helped you on your journey!')
    Replay()


def Replay():
    #Will ask the User if there is another question to be answered
    print ('Do you have another question that I can answer? [Y/N] ')
    reply = input()

    if reply == 'Y':
        Solstice()
    elif reply == 'N':
        exit()
    else:
        print('My apologies, I did not understand your response. Please can you repeat your answer.')
        Replay()


Solstice()
