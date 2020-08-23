

""" import necessary modules """

import re
import random as rnd
import webbrowser as web
import wikipedia as wiki


""" Define Dictionary with set of qstions and answer """

i=rnd.randrange(rnd.randint(1,20))

res={"who are you?":["the names veronica","Veronica"],
     "how old are you?":["i dont know accurately..","2 years more than at your time of birth"],
     "what is your age?":["i was created yesterday",'i dont know my age','it is still a mystery....',"{} years more than at your time of birth".format(i)],
     "who created you?":['my creators are very good human beings.','humans have created me to make their work easy'],
     "how are you?":['i am fine thank you','best as always',"pretty well",'i am ok'],
     "how can you help me?":["i can help you in many ways.. like opening a website, searching stuffs in wikipedia and google,todays date and current time and many more"],
     "that's cool":['indeed it is',"ofcourse it is isn't it"],"thats cool":['indeed it is',"ofcourse it is.. isn't it"]
     }

""" Define one single argument function """
def respond(x):
    if x in res:
        ans=rnd.choice(res.get(x))
        print(ans)
    else:
        print("i didn't get you...")

""" call the above defined function via main """

if "__main__":
    print("Welcome buddy ")
    nm=str(input("what should i call you?: "))
    print('hello {} how can i assist you?: '.format(nm))

    while True:
        z=input("you: ")
        z=z.lower()

        if z=='exit' or z=='bye':
            print('Bye! see you soon')
            break
        elif re.search(r"open",z):
            print('opening {}'.format(z.split('open ')[1]))
            web.open_new_tab( ('www.'+z.split('open ')[1]) )
        elif re.search(r'search',z):
            print('searching wikipedia')
            o=z.split('search')[1]
            print(wiki.summary(o))
        else:
            respond(z)
            

""" start one infinite loop inside main to take inputs continuously """

