## This is the init code for HW3

def getQuestion():
    question = input("What is your question?")
    return question


while keep_asking:
    question_content = getQuestion()
    
    if question[-1] != "?":
        print("I’m sorry, I can only answer questions.")
    elif question == "quit":
        keep_asking = False
    else:
        print(random.choice(answerlist))
