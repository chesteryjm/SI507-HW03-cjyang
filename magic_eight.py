## This is the init code for HW3
import random

def getQuestion():
    question = input("What is your question?")
    return question

magic_ball_answers = ["It is decidedly so","It is certain","Without a doubt",
                      "Yes - definitely","You may rely on it",
                      "As I see it, yes","Most likely","Outlook good",
                      "Yes","Signs point to yes",'Reply hazy, try again.',
                      'Ask again later.', 'Better not tell you now.',
                      'Cannot predict now.','Concentrate and ask again.',
                      'Don\'t count on it.', 'My reply is no.', ' My sources say no.',
                      'Outlook not so good.','Very doubtful.']
keep_asking = True



while keep_asking:
    question = getQuestion()


    if question == 'quit':
        keep_asking = False
    elif question[-1] != "?":
        print("I’m sorry, I can only answer questions.")
    else:
        print(random.choice(magic_ball_answers))
