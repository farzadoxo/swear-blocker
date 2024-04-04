
swears = ['fuck'] # List of swears and bad words

# FUNCTIONAL 

user_input = input("Please enter a text :")

def text_scan(text:str):
    # user most enter a text for scan by this function
    if text in swears:
        print("This text itself is a curse.!!!")
    else:
        counter = 0 # To prevent consecutive responses for texts containing several swear words
        word = text.split(' ') # list words by ' ' (space) 
        for i in word:
            for j in swears:
                if i == j:
                    counter += 1 
                    # But you can use 'Break' !
                    if counter == 1:
                        print("This text contains bad words!")
                        break



# NORMAL


if user_input in swears:
    print("This text itself is a curse.!!!")
else:
    counter = 0 #To prevent consecutive responses for texts containing several swear words
    word = user_input.split(' ') # list words by ' ' (space) 
    for i in word:
        for j in swears:
            if i == j:
                counter += 1 
                # But you can use 'Break' !
                if counter == 1:
                    print("This text contains bad words!")
                    
