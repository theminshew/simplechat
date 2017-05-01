age = raw_input (" How old are you? ")
weight = raw_input (" How much do you weigh? ")
real_weight = raw_input (" No really, how much do you really weigh? ")
print " Hmm, ok lets see what I can do with that?"
import time
time.sleep(3)
print "Gimme a moment, I'm still crunching numbers"
time.sleep(3)
honest_answer = int (real_weight) - 10
fudged_answer = int (real_weight) - 25

#print "ok how does this look? %s is that number better?" % honest_answer

def menu():
    print "ok how does this look? %s is that number better?" % honest_answer
    menu = raw_input("1.) Yes \n2.) No\n")

    if menu == 1:
        letsmoveon()

    elif menu == 2:
        recalculate()

    else:
        print "That is not an option, Please choose 1 or 2."

def recalculate():
    print "Picky, ok let's try again, %s is that number ok?" % fudged_answer

def letsmoveon():
    print "Excellent, Glad I could find a number that works"
    time.sleep(3)

def menu():
    menu = raw_input("1.) Yes \n2.) No\n")
    time.sleep(3)

    if menu == 1:
        abouttime

    elif menu == 2:
        letsmoveon()

    else:
        print "That is not an option, Please choose 1 or 2."

    def abouttime():
        print "Geez, about time"

    def letsmoveon():
        print "Excellent, Glad I could find a number that works"
        time.sleep(3)

print " Alright, so you're %s old and weigh about '%r' " % (
age, honest_answer)

def menu():
    print ("are those numbers about right?")
    menu = raw_input("1.) Yes \n2.) No\n")

    if menu == 1:
        good()

    if menu == 2:
        bad()

def good():
    print ("Ok, based on those calculations I think you're a 10 ")
    time.sleep(1)
    print
    print "hope this made you smile"

def bad():
    print ("I am sorry if I offended you, I am going to leave now")

menu()
